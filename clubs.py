from pyscript import display
from js import document

# specifying dictionaries
clubs = {
    "Art": {
        'Description': 'A club for creative students who enjoy drawing, painting, and designing.',
        "Meeting Time": "11-12AM",
        "Location": "Room 419",
        "Club Moderator": "Ainah",
        "Members": 16
    },
    "Science": {
        "Description": "A club for students who enjoy experiments, robotics, and research.",
        "Meeting Time": "11-12AM",
        "Location": "Room 420",
        "Club Moderator": "Josh",
        "Members": 19
    },
    "Math": {
        "Description": "A club for students who like problem-solving, math contests, and logic puzzles.",
        "Meeting Time": "11-12AM",
        "Location": "Room 421",
        "Club Moderator": "Cortez",
        "Members": 20
    }
}

# to display information when selected in dropdown
def clubInfo(event):
    selected = document.getElementById("schoolClub").value
    info = clubs[selected]   

# to avoid overlapping
    document.getElementById("output").innerHTML = ""              

    display(f"{selected} Club Information", target="output")
    display(f"• Description: {info['Description']}", target="output")
    display(f"• Meeting Time: {info['Meeting Time']}", target="output")
    display(f"• Location: {info['Location']}", target="output")
    display(f"• Club Moderator: {info['Club Moderator']}", target="output")
    display(f"• Number of Members: {info['Members']}", target="output")
