## MiniSocialMedia
[Star Repo]


## Introduction
This is a small try for making a Social Media using python Tkinter,  
As a final assignment of 

### Algorithm and Data Structures.


I have tried my best to implement this project as MVC architecture.\
All the application logic will be on the app directory.\
Each view will have its own respective Controller on the controllers\
directory under app directory.

The project folder is as shown below

> .  
> ├── app  
> │   ├── Controllers  
> │   │   ├── FriendsController.py  
> │   │   ├── FriendsController_test.py  
> │   │   ├── LoginController.py  
> │   │   ├── MessageController.py  
> │   │   ├── PostController.py  
> │   │   ├── README.md  
> │   │   ├── RegisterController.py  
> │   │   ├── Server.py  
> │   │   └── UserController.py  
> │   ├── Friends.py  
> │   ├── LoginRegister.py  
> │   ├── LoginRegister_test.py  
> │   ├── Messages.py  
> │   ├── Post.py  
> │   ├── README.md  
> │   └── User.py  
> ├── codeCount  
> ├── Config  
> │   ├── check.py  
> │   ├── config.py  
> │   └── image_works.py  
> ├── LICENSE  
> ├── loggedin  
> ├── marksAsPerTopics  
> ├── README.md  
> ├── requirements.txt  
> ├── resources  
> │   ├── assets  
> │   │   └── default_avatar.png  
> │   └── views  
> │       ├── AddPost.py  
> │       ├── AllPosts.py  
> │       ├── clear_widgets.py  
> │       ├── Friends.py  
> │       ├── home.py  
> │       ├── login.py  
> │       ├── Message.py  
> │       ├── OpenPost.py  
> │       └── register.py  
> ├── routes  
> │   ├── index.py  
> │   └── README.md  
> ├── run_me_client.py  
> ├── server.py  
> └── validation  
>     ├── core_validation.py  
>     ├── core_validation_test.py  
>     ├── README.md  
>     └── send_to_server.py  
>  
> 8 directories, 43 files  

## Run as

- virtualenv venv \
  source venv/bin/activate \
  pip install -r requirements.txt

- python3 server.py start ( to start the instance of the server)

- python3 run_me_client.py ( to start the instance of the client)



[Star Repo]: https://github.com/leodahal4/MiniSocialMedia
