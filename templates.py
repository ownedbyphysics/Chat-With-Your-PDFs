css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #8490a9
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://media.istockphoto.com/id/1221348467/vector/chat-bot-ai-and-customer-service-support-concept-vector-flat-person-illustration-smiling.jpg?s=612x612&w=0&k=20&c=emMSOYb4jWIVQQBVpYvP9LzGwPXXhcmbpZHlE6wgR78=" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://static-00.iconduck.com/assets.00/user-icon-2048x2048-ihoxz4vq.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''