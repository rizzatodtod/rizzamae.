import requests
import streamlit as st 
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/101e12ec-fdf3-4faa-8ffe-4f4a4249a14e/0udkFWUe9U.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Rizza Mae A. Todtod :wave:")
    st.title("How To Overcome The Challenges In Computer Engineering")
    st.write("To overcome challenges in computer engineering, it is essential to continuously learn and stay updated with the latest technologies, develop strong fundamentals, approach problems with a systematic mindset, collaborate with others, gain hands-on experience, embrace failure as a learning opportunity, manage time effectively, and maintain persistence and motivation. By combining these strategies, one can navigate the complexities of computer engineering and successfully overcome challenges in the field.")
    st.write("[Learn More >](https://files.eric.ed.gov/fulltext/ED577147.pdf)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            How to Overcome the challenges of being a Computer Engineer:
            - CONTINOUOS LEARNING: To keep up with the newest technological advancements and trends, habitually read research papers, technical blogs, and articles.

            - PROBLE SOLVING SKILLS: To enhance problem-solving skills, seek advice from mentors and work alongside colleagues to gain fresh perspectives.

            - ADAPTABILITY: To take on new challenges, be willing to step out of your comfort zone and embrace changes.

            - COMMUNICATION SKILLS: In any engineering position, it is vital to have effective communication skills. Being able to express technical information in a concise and clear manner is necessary both orally and in writing.

            - TIME MANAGEMENT: Prioritizing tasks, managing time efficiently, and setting realistic deadlines are all crucial when dealing with the demanding workload of computer engineering. To prevent getting swamped, it's wise to break down massive assignments into more manageable segments and deal with them individually.

            - SOFT SKILL DEVELOPMENT: Engage in conversations, with your colleagues and mentors to receive feedback and pinpoint areas where you can enhance your skills. Take steps to actively develop and improve these skills.

            - WORK-LIFE BALANCE: Achieving long term success requires finding a balance, in life. It's important to avoid burnout by taking care of yourself both at work and, in your life. Make sure to take breaks prioritize self care and make time for your hobbies and things that bring you joy.
            """
    )
    st.write("[Learn More >](https://www.knowledgehut.com/blog/web-development/software-engineer-challenges)")

# Define right_column here before using it
right_column = st.columns(2)[1]

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me !:")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Yourname" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="mmessage" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
