
# Import system
import sys

# Import QtCore and QtWidgets
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFormLayout, QWidget, QStackedWidget, QSpinBox, QPlainTextEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout, QSizePolicy
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

# Import functions from other classes
from RedditGetter import GetRedditPost
from ChatGPT import ChatGPT_Prompt

# Create a layout for Home Page
class HomeWidget(QWidget):
    # Intialize FUnction
    def __init__(self, parent=None):
        # Intialialize HomeWidge
        super().__init__(parent)

        # Create form for layout
        home_layout = QVBoxLayout()

        # Intialize values
        self.reddit_url = ""
        self.number_of_comments = 0
        self.chat_gpt_prompt = ""

        # Reddit Url
        self.reddit_url_input = QLineEdit()
        self.reddit_url_input.textChanged.connect(self.updateUrl)
        home_layout.addWidget(self.reddit_url_input, alignment=Qt.AlignmentFlag.AlignVCenter)

        # Number of Comments
        self.number_of_comments_input = QSpinBox()
        self.number_of_comments_input.valueChanged.connect(self.updateInput)
        home_layout.addWidget(self.number_of_comments_input, alignment=Qt.AlignmentFlag.AlignVCenter)

        # Chapt GPT Prompt
        self.chat_gpt_prompt_input = QPlainTextEdit()
        self.chat_gpt_prompt_input.textChanged.connect(self.updatePrompt)
        home_layout.addWidget(self.chat_gpt_prompt_input, alignment=Qt.AlignmentFlag.AlignVCenter)

        # Submit button
        self.submit_button = QPushButton("Submit")
        home_layout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignVCenter)
        
        
        # Set the layoout
        self.setLayout(home_layout)

    # Changes the text for the url
    def updateUrl(self, text):
        # Get the text of the url and set it to reddit_url_input
        self.reddit_url = text

    # Update input
    def updateInput(self, value):
        # Get the value 
        self.number_of_comments = value

    # Get text for prompt 
    def updatePrompt(self):
        # Get the text
        self.chat_gpt_prompt = self.chat_gpt_prompt_input.toPlainText()

# Create a widget for editing final prompt
class FinalTextWidget(QWidget):
    # Intialize FUnction
    def __init__(self, parent=None):
        # Intialialize HomeWidge
        super().__init__(parent)

        # Create layout
        layout = QFormLayout()

        # Intialize values
        self.final_text = ""
        self.redo_prompt = ""

        # Back Button
        self.backButton = QPushButton("Back")
        layout.addRow(self.backButton)

        # Final Text Editor
        self.final_text_input = QPlainTextEdit()
        self.final_text_input.textChanged.connect(self.updateFinalText)
        layout.addRow("Final Text", self.final_text_input)

        # Redo Prompt
        self.redo_prompt_input = QPlainTextEdit()
        self.redo_prompt_input.textChanged.connect(self.updateRedoPrompt)
        self.redo_button = QPushButton("Redo")
        self.redo_widget = QHBoxLayout()
        self.redo_widget.addWidget(self.redo_prompt_input)
        self.redo_widget.addWidget(self.redo_button)
        layout.addRow("Redo Prompt", self.redo_widget)

        # Continue button
        self.continueButton = QPushButton("Continue")
        layout.addRow(self.continueButton)

        # Set layout
        self.setLayout(layout)

    # Change final test_input
    def updateFinalText(self):
        # Get the text from input and store it in final_text
        self.final_text = self.final_text_input.toPlainText()
    
    # Change the redo prompt input
    def updateRedoPrompt(self):
        # Get the text from input and store it in redo_prompt
        self.redo_prompt = self.redo_prompt_input.toPlainText()

# Create a widget for video and voice
class VoiceVideoWidget(QWidget):
    # Intialize FUnction
    def __init__(self, parent=None):
        # Intialialize HomeWidge
        super().__init__(parent)

        # Create layout
        layout = QFormLayout()

        # Intialize vlaues
        self.choice = ""
        self.youtube_url = ""

        # Back Button
        self.backButton = QPushButton("Back")
        layout.addRow(self.backButton)

        # Create buttons for choosing voices
        self.createButtons()

        # Create buttons and add it to layout
        layout.addRow("Voices", self.gridLayout)

        # Url to youtube link
        self.youtube_url_input = QLineEdit()
        self.youtube_url_input.textChanged.connect(self.updateYoutubeUrl)
        layout.addRow("Youtube URL", self.youtube_url_input)

        # Set Create Video Button
        self.create_video_button = QPushButton("Create Video")
        layout.addRow(self.create_video_button)

        # Set layout
        self.setLayout(layout)
        
    # Set youtube url
    def updateYoutubeUrl(self, text):
        # Set youtube_url to text
        self.youtube_url = text
    # Create the buttons
    def createButtons(self):
        # Create Grid Laylout
        self.gridLayout = QGridLayout()

        # Create a list of buttons
        self.buttons = []

        # Create list of choices
        voice_name = ["Biden", "Trump", "Freeman", "Rogan", "Musk", "Dumbledore", "Elizabeth", "Ferrell"]

        # For i in 8
        for i in range(8):
            # Caculate the row and columen based on i
            row = (int)(i / 2) + 1
            column = (i % 2) + 1

            # Get the name
            name = voice_name[i]

            # Create a push button
            button = QPushButton(name, self)
            button.setStyleSheet(
                "background-color : white;"
            )
            button.clicked.connect(lambda ch, i=i, name=name: self.updateChoice(name, i))
        
            # Add button to gridLayer
            self.gridLayout.addWidget(button, row, column)

            # Push buttons
            self.buttons.append(button)

    
    # Update choice
    def updateChoice(self, text, i):
        # Set choice to text
        self.choice = text

        # Go through each button in buttons
        for j in range(len(self.buttons)):
            # If j is i
            if j == i:
                # Enable button
                self.buttons[j].setStyleSheet(
                "background-color : lightblue;"
            )
            # Othewise
            else:
                # Unenable button
                self.buttons[j].setStyleSheet(
                    "background-color: white"
                )

# Final Page 
class FinalVideoWidget(QWidget):
    # Intialize FUnction
    def __init__(self, parent=None):
        # Intialialize HomeWidge
        super().__init__(parent)

        # Create layout
        layout = QHBoxLayout()
        video_layout = QVBoxLayout()
        self.choice_layout = QVBoxLayout()

        # Create movie 
        self.media_player = QMediaPlayer()
        self.media_player.setSource(QUrl.fromLocalFile("final_video.mp4"))
        self.video_widget = QVideoWidget()
        
        self.media_player.setVideoOutput(self.video_widget)
        self.video_widget.adjustSize()
      
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_video)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_video)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_video)

        video_layout.addWidget(self.video_widget)
        video_layout.addWidget(self.start_button)
        video_layout.addWidget(self.pause_button)
        video_layout.addWidget(self.stop_button)

        layout.addLayout(video_layout)

        # Buttons Layout
        # Back Button
        self.back_button = QPushButton("Go Back")
        self.choice_layout.addWidget(self.back_button)
        
        # Youtube Button
        self.upload_to_youtube_button = QPushButton("Upload to Youtube")
        self.choice_layout.addWidget(self.upload_to_youtube_button)

        # TikTok Button
        self.upload_to_tiktok_button = QPushButton("Upload to Titok")
        self.choice_layout.addWidget(self.upload_to_tiktok_button)

        # New Video 
        self.new_video_button = QPushButton("New Video")
        self.choice_layout.addWidget(self.new_video_button)

        # Add Buttons Layout
        layout.addLayout(self.choice_layout)
        self.setLayout(layout)


    def start_video(self):
        self.media_player.play()

    def pause_video(self):
        self.media_player.pause()

    def stop_video(self):
        self.media_player.stop()

# Define the main layout
# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        # Super intialize
        super().__init__()

        # Window Ttile
        self.setWindowTitle("Racer")

        # Set central widge
        self.central_widget = QStackedWidget()

        # Set central widget
        self.setCentralWidget(self.central_widget)

        # Set widgets
        self.home_widget = HomeWidget(self)
        self.final_text_widget = FinalTextWidget(self)
        self.voice_video_widget = VoiceVideoWidget(self)
        self.final_video_widget = FinalVideoWidget(self)

        # Submit Butotn
        self.home_widget.submit_button.clicked.connect(self.runPrompts)

        # Redo Button
        self.final_text_widget.redo_button.clicked.connect(self.redoPrompt)

        # Back Buttons
        self.final_text_widget.backButton.clicked.connect(lambda: self.switchPage(0))
        self.voice_video_widget.backButton.clicked.connect(lambda: self.switchPage(1))
        self.final_video_widget.back_button.clicked.connect(lambda: self.switchPage(2))
        
        # Create New Video Button
        self.final_video_widget.new_video_button.clicked.connect(lambda: self.switchPage(0))

        # Continue Buttons
        self.final_text_widget.continueButton.clicked.connect(lambda: self.switchPage(2))

        # Add pages
        self.central_widget.addWidget(self.home_widget)
        self.central_widget.addWidget(self.final_text_widget)
        self.central_widget.addWidget(self.voice_video_widget)
        self.central_widget.addWidget(self.final_video_widget)
    

    # Make text with prompt 
    def makeText(self, content, prompt):
        # Make edited post by modifying result using the chat gpt prompt
        edited_post = ChatGPT_Prompt(prompt, content)
        edited_post = edited_post['choices'][0]['text']

       # Splited edited post with new lines
        edited_post_list = edited_post.split("\n")
        
        # Loop through each item in edited_post_list
        edited_post = ""
        for i in range(len(edited_post_list)):
            # If post is ''
            if(edited_post_list[i] != ''):
                # Add everything after post
                edited_post = '\n'.join(edited_post_list[i:])
                break

        # Set text of final edit and prompt 
        self.final_text_widget.final_text_input.setPlainText(edited_post)
        self.final_text_widget.final_text = edited_post
        self.final_text_widget.redo_prompt_input.setPlainText(prompt)
        self.final_text_widget.redo_prompt = prompt
        
    # Run ChatGpt Prompt 
    def runPrompts(self):
        # Get the url, number_of_comments, and prompt
        reddit_url = self.home_widget.reddit_url
        number_of_comments = self.home_widget.number_of_comments
        chat_gpt_prompt = self.home_widget.chat_gpt_prompt

        # Send them to chat_gpt
        content = GetRedditPost(reddit_url, number_of_comments)
        
        # Create the text of comments
        comments = ''

        # Go through each comment from content and add them to comments
        for i in range(number_of_comments):
            comments += f"\n{content['comments'][i]['comment_body']}"
        
        # Forment content in this format
        # Title: Title Of Post
        # Body: Body of Post
        # Comments: Comments on the post
        Result = f"Title: {content['title']}\nBody: {content['body']}\nComments: {comments}"
    
        # Make text with body and prompt
        self.makeText(Result, chat_gpt_prompt)

        # Switch to final_text_widget
        self.central_widget.setCurrentIndex(1)

    # Redo button
    def redoPrompt(self):
        # Get text and prompt
        content = self.final_text_widget.final_text
        prompt = self.final_text_widget.redo_prompt

        # Make text 
        self.makeText(content, prompt)

    # Go back to previous page
    def switchPage(self, i):
        # Switch to page based on i
        self.central_widget.setCurrentIndex(i)
        
# Main Function
if __name__ == "__main__":
    # Set Application
    app = QApplication(sys.argv)

    # Set Window
    window = MainWindow()
    window.show()

    # Execute App
    app.exec()

