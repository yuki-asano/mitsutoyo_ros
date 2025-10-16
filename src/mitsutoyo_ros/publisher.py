#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
from mitsutoyo_ros.mitsutoyo_interface import MitsutoyoInterface


pub = rospy.Publisher('micrometer_thickness', Float32, queue_size=10)
rospy.init_node('micrometer_publisher')

mi = MitsutoyoInterface()


while not rospy.is_shutdown():
    value = mi.get_value_by_button()
    pub.publish(value)
