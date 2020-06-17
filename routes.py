
from flask import Flask, render_template, url_for, flash, redirect
from flask_assignment.forms import PostForm
from flask_sqlalchemy import SQLAlchemy
from flask_assignment.models import Post
from flask_assignment import db ,app
from flask import render_template, url_for, flash, redirect, request, abort

@app.route("/home")
@app.route("/")
def home():
    post = Post.query.all()
    return render_template('home.html',posts=post)
@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('home.html', title='About')
@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('home.html', title='About')
@app.route("/logout")
def logout():
    return render_template('home.html', title='About')
@app.route("/about")
def about():
    return render_template('home.html', title='About')

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route("/postm",methods =['GET','POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,content = form.content.data)
        db.session.add(post)
        db.session.commit()
        flash(f'Post have been created','success')
        return redirect(url_for('home'))
    return render_template('create_post.html',title = 'New post',form =form)

@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')

@app.route("/post/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))
if __name__ == '__main__':
   app.run(debug=True)