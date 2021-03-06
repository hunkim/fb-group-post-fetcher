import os
from dotenv import load_dotenv

load_dotenv()

GROUP_ID    = os.getenv("FB_GROUP_ID")
BASE_URL    = f"https://graph.facebook.com/v7.0/{GROUP_ID}/feed?"
TAIL_URL    = f"fields=message%2Creactions.summary(total_count)%2Ccomments.summary(total_count)%2Cpermalink_url%2Cshares%2Cupdated_time%2Cattachments{{media}}"
SMTP_USER   = os.getenv("SMTP_USER")
SMTP_PASS   = os.getenv("SMTP_PASS")

TOP_K       = int(os.getenv("TOP_K"))
FIRST_WORDS = int(os.getenv("FIRST_WORDS"))

HEAD_LOGO   = "https://cdn-images-1.medium.com/max/1600/0*LDGNE2IRJOFFcJ3s.png"
HEAD_IMAGE  = "https://github.com/deep-diver/fb-group-post-fetcher/blob/master/static/images/tfkr-logo-white-background.png?raw=true"
HEAD_ARTICLE= "텐서플로우 한국 커뮤니티 (TFUG Korea) 에서 발행하는 뉴스레터 입니다. 지난 몇 일간 게시된 글 중, 좋아요/공유/댓글 개수를 산정하여 TOP 10으로 랭킹된 것들을 모아서 보내드립니다. 자세한 내용은 하단을 참고해 주시고, 더 많은 게시글을 보고 싶으시다면 커뮤니티 방문하기 버튼을 클릭해 주세요!"
HEAD_BUTTON_TITLE = "커뮤니티 방문하기"
BOTTOM_ARTICLE= "현재 시범 운영 중입니다"