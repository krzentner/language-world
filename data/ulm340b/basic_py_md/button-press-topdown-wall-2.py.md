

You must call the `robot.check()` function at most 8 times in your program.

## Answer

# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    if check("the robot's gripper is not vertically aligned with the button and the robot's gripper is below the button"):
        robot.place("gripper above button")
    if check("the robot's gripper is vertically aligned with button and gripper is above button"):
        robot.push("down on button")
[eod] [code]from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import User, Post, Like, Dislike
from .forms import PostForm

@login_required(login_url='/accounts/login/')
def user_page(request):
	context = {
		'request': request,
		'user_list': User.objects.all(),
	}
	return render(request, 'users/user.html', context)

@login_required(login_url='/accounts/login/')
def user_post(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	post_list = Post.objects.filter(user_id=user_id)
	context = {
		'request': request,
		'user': user,
		'post_list': post_list,
	}
	return render(request, 'users/post.html', context)

@login_required(login_url='/accounts/login/')
def post_create(request, user_id):
	post_form = PostForm(request.POST or None, request.FILES or None)
	if post_form.is_valid():
		post_form.instance.user_id = user_id
		post_form.save()
		messages.success(request, f"성공적으로 포스트를 생성하였습니다.")
	return redirect('user_post', user_id=user_id)

@login_required(login_url='/accounts/login/')
def post_like(request, post_id):
	current_user = request.user
	if Like.objects.filter(