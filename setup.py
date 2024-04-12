from setuptools import find_packages, setup

setup(
    name="multilingual assistant",
    version="0.0.1",
    author="kamlesh",
    author_email="kamleshpadwal@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)