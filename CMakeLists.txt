cmake_minimum_required(VERSION 2.8.0)
project(mitsutoyo_ros)

find_package(catkin REQUIRED COMPONENTS
  std_msgs
  rospy
)

catkin_python_setup()

catkin_package()

catkin_install_python(
  PROGRAMS
  scripts/get_value_by_cmd.py
  scripts/get_value_by_button.py
  DESTINATION
    ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(
  DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/
  )
