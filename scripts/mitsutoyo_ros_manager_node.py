#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from mitsutoyo_ros.mitsutoyo_ros_manager import MitsutoyoROSManager


if __name__ == '__main__':
    rospy.init_node('mitsutoyo_ros_manager_node')
    mrm = MitsutoyoROSManager()

    while not rospy.is_shutdown():
        mrm.publisher()
