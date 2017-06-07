# MIT_projects
Python implementation of a case study in Module 1 in MITProfessionalX's course "Data Science: Data to insights". 
The case study is: "Module 1 - Making sense of unstructured data  Case Study". Case study is about doing our own analysis on MIT EECS
faculty data using stochastic variational inference on LDA. T
If you can access it, the description of the project is here:

[Self-Help Documentation](http://mitprofessionalx.mit.edu/asset-v1%3aMITProfessionalX+DSx+2017_T2+type@asset+block@Module1_CS2_LDA-analysis.pdf)

---

## Run the script
Clone the master branch and run it with e.g.:

`python scrape.py`


A dialog for the "Solitaire" mode is shown. Choose the usernames and colors for the two players and click on "Start": 

![alt text](https://github.com/aless80/tantrix/blob/master/img/SolitaireDialog.png "Solitaire dialog")

The tantrix game will be started:

![alt text](https://github.com/aless80/tantrix/blob/master/img/tantrix_game_solitaire.png "Tantrix")

## Launch server and two tantrix clients
Clone the master branch on both computers. One computer will need an open port to start the server:

`python server.py <host>:<port>`

![alt text](https://github.com/aless80/tantrix/blob/master/img/terminal_server.png "python server.py")

Both computers start tantrix.py with:

`python tantrix.py <host>:<port>`

![alt text](https://github.com/aless80/tantrix/blob/master/img/terminal_client1.png "terminal client1.py")

![alt text](https://github.com/aless80/tantrix/blob/master/img/terminal_client2.png "terminal client2.py")

The default host and port are localhost and 31425, respectively. In this way server.py and tantrix.py can be run on one computer.


Once both clients are connected, a "waiting room" dialog will popup and display on all clients all connected clients:

![alt text](https://github.com/aless80/tantrix/blob/master/img/WaitingRoom_client1.png "waiting room.py")

Select your username and color, chat with the other clients and press "ready":

![alt text](https://github.com/aless80/tantrix/blob/master/img/WaitingRoom_client1_ready.png "client1 ready")

Once two clients are ready, the game will start:


![alt text](https://github.com/aless80/tantrix/blob/master/img/tantrix_game_2players.png "tantrix game 2 players")


---

## Commands in the game

Use the mouse to move tiles. You are free to move any tile on the board, but you will have to confirm your move (hit the Confirm button or Return) to move on. When playing with another client over the server, your tiles will be reset once your opponent confirms a move. A message above/below your tiles will show the current status and 

| Command        | Function       | Button     |
| ------------- |:-------------:|:-------------:|
| Return | Confirm your move | Confirm |
| Left mouse click on a tile | Rotate tile clockwise | |
| Left mouse click on an empty space | Highlight which tiles fit in the hexagon | |
| Right mouse click on a tile | Rotate tile anti-clockwise | |
| R | Reset (bring all tiles back to original place) | Reset |
| Ctrl + W | Quit the game | Quit |
| Ctrl + Q | Quit the game | Quit |
| Up/Down/Left/Right Arrows | center the played tiles (if applicable) | |
| S | Show the score | Score |