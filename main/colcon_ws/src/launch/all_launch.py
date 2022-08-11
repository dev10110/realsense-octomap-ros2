#!/usr/bin/env python
import os.path as osp

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription, logging
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import \
    PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import ThisLaunchFileDir


def generate_launch_description():
    # rviz

    rviz_node = Node(
            package='rviz2',
            namespace='',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', '/root/colcon_ws/src/launch/config.rviz']
        )

    # Octomap
    octomap_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([osp.join(
               get_package_share_directory('octomap_server2'), 'launch'),
                '/octomap_server_launch.py'])
            )

    ## Realsense
    realsense_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([osp.join(
                get_package_share_directory('realsense2_camera'),'launch'),
                '/rs_launch.py']),
            launch_arguments = {
                'pointcloud.enable': 'true',
                'decimation': '8',
                'clip_distance': '1.0'
                }.items()
            )

    return LaunchDescription([
        realsense_launch,
        octomap_launch,
        rviz_node
        ])
