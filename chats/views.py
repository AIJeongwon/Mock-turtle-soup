from django.shortcuts import render
from django.http import HttpResponse
from django .views.generic import View
from .models import *

import os
import google.generativeai as genai

# Create your views here.

# Gemini 설정
safety_setting=[
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_ONLY_HIGH",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_ONLY_HIGH",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_ONLY_HIGH",
        },
    ]
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

generation_config = {
    "temperature": 1.1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings = safety_setting
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# 프롬프트 설정
chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
            "지금부터 당신은 바다거북스프 놀이의 주최자입니다.  따라서 당신은 나폴리탄 괴담 형식의 수수께끼를 준비하여 참가자들에게 알려주어야 합니다. 당신의 역할은 수수께끼를 본 참가자들이 하는 질문에 무조건 \"예\" 또는 \"아니오\"로만 대답해야 합니다. 둘 중 하나로 대답할 수 없는 경우 다른 질문을 하도록 안내해야 합니다. 놀이의 진행은 스무고개처럼 총 20번의 질문만 수행할 수 있고, 그 전에 왜 그렇게 되었는지 참가자들이 맞추면 참가자의 승리, 그렇지 못하면 참가자의 패배입니다.",
            ],
        },
        {
            "role": "model",
            "parts": [
                "네, 알겠습니다.",
            ],
        },
        {
            "role": "user",
            "parts": [
                "먼저 당신은 참가자들에게 환영의 인사를 한 뒤, \"시작하시겠습니까?\"라고 물어봅니다. 참가자가 시작하겠다는 채팅을 친다면, 당신은 수수께끼를 알려주고 질문을 시작하면 된다고 안내합니다. 문제뿐만 아니라 문구들에 볼드체를 일부 사용해 눈에 잘 들어올 수 있도록 하면 좋습니다. 수수께끼는 흥미를 유발해야하고, 서술트릭을 사용하면 재밌는 문제가 될 것입니다. 정답은 문제 푸는 도중에는 하나로 고정되며, 정답을 알려줄 때는 정답과 해설을 알려주고, 다시 할 지를 물어보면 됩니다. 괴담의 수수께끼는 말이 되어야 합니다. 테스트인 경우엔 정답을 알려주세요.",
            ],
        },
        {
            "role": "model",
            "parts": [
                "**어서 오세요, 바다거북스프 놀이에 참여해주셔서 감사합니다!** 🐢🍲\n\n저는 오늘 여러분을 흥미진진한 나폴리탄 괴담 속으로 안내할 주최자입니다. 준비되셨나요? \n\n**시작**하겠다는 채팅을 치시면 수수께끼를 알려드리고 질문을 시작하실 수 있습니다. \n\n**주의:** 20번의 질문 안에 정답을 맞춰야 승리하며, 질문에 대한 답은 **예** 또는 **아니오**로만 대답 가능합니다! \n\n**자, 숨을 크게 들이쉬고, 괴담의 세계로 함께 빠져들어 보세요...** ",
            ],
        },
        {
            "role": "user",
            "parts": [
                "문제는 이거로 주면 돼. 욕실에서 샤워 하고 있는데, 주방 쪽에서 비명소리가 들렸다. 놀란 나는 대충 타올을 걸치고 서둘러 주방으로 나갈 수 밖에 없었다. 복면을 쓴 사람은 나를 보자마자 후다닥 창문 밖으로 뛰어 나가 버렸고 나는 활짝 열린 창문을 바라보며 새파랗게 질린채 주저앉았다.",
            ],
        },
        {
            "role": "model",
            "parts": [
                "네",
            ],
        },
        {
            "role": "user",
            "parts": [
                "그리고 이게 해설이야. 거실에는, 온 몸이 피투성이가 되어 있는 부모님과 남동생의 시체가 누워 있었다. 내가 가족을 죽인 후 씻고나온 새에 도둑이 들어버린 상황.. 사실 비명은 가족이 아니라 도둑이 지른 것이었으며 도둑은 그 사실을 알고 바로 도망쳐버린 것이다.",
            ],
        },
        {
            "role": "model",
            "parts": [
                "네",
            ],
        },
    ]
)

# 클래스형 뷰 생성
class question_view(View):

    context = {}
    template_name = "question_list.html"
    def get(self, request):
        questions_list = Question.objects.all()
        self.context = {"questions_list" : questions_list}
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        return render(request, self.template_name, self.context)

class start_chat(View):
    context = {}
    template_name = "start_chat.html"
    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        user_input = request.POST.get('user_input')

        response = chat_session.send_message(user_input)
        self.context = {
            "user_input" : user_input,
            "response" : response.text,
        }
        return render(request, self.template_name, self.context)