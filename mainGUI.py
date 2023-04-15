
# Import system
import sys

# Import QtCore and QtWidgets
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFormLayout, QWidget, QStackedWidget, QSpinBox, QPlainTextEdit, QPushButton, QHBoxLayout, QVBoxLayout

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
        home_layout = QFormLayout()

        # Intialize values
        self.reddit_url = ""
        self.number_of_comments = 0
        self.chat_gpt_prompt = ""

        # Reddit Url
        self.reddit_url_input = QLineEdit()
        self.reddit_url_input.textChanged.connect(self.updateUrl)
        home_layout.addRow("Reddit URL", self.reddit_url_input )

        # Number of Comments
        self.number_of_comments_input = QSpinBox()
        self.number_of_comments_input.valueChanged.connect(self.updateInput)
        home_layout.addRow("Number Of Comments", self.number_of_comments_input)

        # Chapt GPT Prompt
        self.chat_gpt_prompt_input = QPlainTextEdit()
        self.chat_gpt_prompt_input.textChanged.connect(self.updatePrompt)
        home_layout.addRow("Chat GPT Prompt", self.chat_gpt_prompt_input)

        # Submit button
        self.submit_button = QPushButton("Submit")
        home_layout.addRow(self.submit_button)
        
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
        self.home_widget.submit_button.clicked.connect(self.runPrompts)
        self.central_widget.addWidget(self.home_widget)
        self.central_widget.addWidget(self.final_text_widget)


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
    
        # Make edited post by modifying result using the chat gpt prompt
        edited_post = ChatGPT_Prompt(chat_gpt_prompt, Result)
        edited_post = edited_post['choices'][0]['text']
        print(edited_post)
        # Set text of final edit and prompt 
        self.final_text_widget.final_text_input.setPlainText(edited_post)
        self.final_text_widget.final_text = edited_post
        self.final_text_widget.redo_prompt_input.setPlainText(chat_gpt_prompt)
        self.final_text_widget.redo_prompt = chat_gpt_prompt

        # Switch to final_text_widget
        self.central_widget.setCurrentIndex(1)

    # Redo button
        
# Main Function
if __name__ == "__main__":
    # Set Application
    app = QApplication(sys.argv)

    # Set Window
    window = MainWindow()
    window.show()

    # Execute App
    app.exec()

