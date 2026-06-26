from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import User, Message
from .forms import MessageForm, UserForm, MessageEditForm
from datetime import datetime, timedelta
from django.utils import timezone


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.id
            return redirect('chat')
    else:
        form = UserForm()

    return render(request, 'chat/register.html', {'form': form})


def home(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('register')

    user = User.objects.filter(id=user_id).first()
    if not user:
        request.session.flush()
        return redirect('register')

    messages_query = Message.objects.filter(is_deleted=False).select_related('user')

    filter_date = request.GET.get('date')
    if filter_date:
        try:
            parsed_date = datetime.strptime(filter_date, '%Y-%m-%d').date()
            messages_query = messages_query.filter(timestamp__date=parsed_date)
        except ValueError:
            pass

    messages_list = messages_query.order_by('-timestamp')
    archived_messages = Message.objects.filter(user=user, is_deleted=True).select_related('user').order_by('-timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = user
            message.save()
            return redirect('chat')
    else:
        form = MessageForm()

    return render(request, 'chat/chat.html', {
        'chat_messages': messages_list,
        'archived_messages': archived_messages,
        'form': form,
        'user': user,
        'filter_date': filter_date
    })


def edit_message(request, pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('register')

    user = get_object_or_404(User, id=user_id)
    message = get_object_or_404(Message, pk=pk)

    if message.user != user:
        return HttpResponseForbidden()

    if message.timestamp < timezone.now() - timedelta(minutes=30):
        messages.error(request, 'Время для редактирования сообщения (30 минут) уже истекло!')
        return redirect('chat')

    if request.method == 'POST':
        form = MessageEditForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение успешно отредактировано!')
            return redirect('chat')
    else:
        form = MessageEditForm(instance=message)

    return render(request, 'chat/edit_message.html', {'form': form, 'message': message})


def delete_message(request, pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('register')

    user = get_object_or_404(User, id=user_id)
    message = get_object_or_404(Message, pk=pk)

    if message.user != user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        message.is_deleted = True
        message.save()
        messages.warning(request, 'Сообщение успешно удалено и перемещено в архив.')
        return redirect('chat')

    return render(request, 'chat/delete_confirm.html', {'message': message})


def restore_message(request, pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('register')

    user = get_object_or_404(User, id=user_id)
    message = get_object_or_404(Message, pk=pk)

    if message.user != user:
        return HttpResponseForbidden()

    message.is_deleted = False
    message.save()
    messages.success(request, 'Сообщение успешно восстановлено!')
    return redirect('chat')