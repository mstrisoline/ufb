from flask import Blueprint, flash, Markup, redirect, render_template, url_for, request
from flask.ext.login import login_required, login_user, logout_user
from jinja2 import TemplateNotFound
from .forms import *
from .models import *

site = Blueprint('site', __name__, template_folder='templates')

@site.route("/")
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@site.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        flash("Welcome")
        return redirect(url_for("site.index"))
    return render_template('login.html', form=form)

@site.route('/register/', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.gen_salt()
        user.set_pw(user.password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('site.index'))
    return render_template('register.html', form=form)

@site.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.login'))

@site.route('/profile/<nickname>', methods=('GET', 'POST'))
@login_required
def profile(nickname=None):
    user = User.query.filter(User.nickname == nickname).first()
    posts = Post.query.filter(Post.user_id == user.id).all()
    form = ProfileForm()
    post_form = PostForm()
    reply_form = ReplyForm()
    return render_template('profile.html', user=user, post_form=post_form, reply_form=reply_form, form=form, nickname=nickname, posts=posts)

@site.route('/submit_post/<int:author_id>/<nickname>', methods=('GET', 'POST'))
@login_required
def submit_post(nickname=None, author_id=None):
    form = PostForm()
    author = User.query.get(author_id)
    if request.method == 'POST':
        if form.validate_on_submit():
            post = Post()
            post.user_id = author_id
            post.body = request.form['post_body']
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('site.profile', nickname=author.nickname))
    return redirect(url_for('site.profile', nickname=author.nickname))

@site.route('/sbumit_reply/<int:post_id>/<int:author_id>', methods=('GET', 'POST'))
@login_required
def submit_reply(post_id=None, author_id=None):
    form = ReplyForm()
    post = Post.query.get(post_id)
    post_owner = User.query.get(post.user_id)
    if request.method == 'POST':
        if form.validate_on_submit():
            author = User.query.get(author_id)
            reply = Reply()
            reply.user_id = author.id
            reply.post_id = post.id
            reply.body = request.form['reply_body']
            db.session.add(reply)
            db.session.commit()
            return redirect(url_for('site.profile', nickname=post_owner.nickname))
    return redirect(url_for('site.profile', nickname=post_owner.nickname))
