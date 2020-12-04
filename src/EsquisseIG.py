#!/usr/bin/env python

import subprocess
import rospy
from std_msgs.msg import String
import Tkinter as tk



def interface_graphique():
	root = tk.Tk()
	canvas1 = tk.Canvas(root, width = 400, height = 300)
	canvas1.pack()
	resultatTb = tk.Entry (root)
	canvas1.create_window(200, 140, window=resultatTb)
	def lancer_launch():
		subprocess.check_call('roslaunch panda_moveit_config demo.launch rviz_tutorial:=true', shell=True)
	button1 = tk.Button(text='lancer fichier launch 1', command=lancer_launch)
	canvas1.create_window(200, 180, window=button1)
	def lancer_commande():
		subprocess.check_call('rosrun moveit_tutorials move_group_python_interface_tutorial.py', shell=True)
	button2 = tk.Button(text='lancer commande robot', command=lancer_commande)
	canvas1.create_window(200, 220, window=button2)
	root.mainloop()

	

rospy.init_node("interface_graphique")

interface_graphique()
#pub = rospy.Publisher("T_Ordre_interface_graphique", String, queue_size=1)
#sub = rospy.Subscriber("T_reception_interface_graphique", String, interface_graphique)
rospy.spin()
