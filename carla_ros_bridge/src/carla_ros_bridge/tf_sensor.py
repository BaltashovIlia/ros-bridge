#!/usr/bin/env python
#
# Copyright (c) 2020 Intel Corporation
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.
#
"""
handle a tf sensor
"""

import rospy

from carla_ros_bridge.pseudo_actor import PseudoActor

import tf


class TFSensor(PseudoActor):

    """
    Pseudo tf sensor
    """

    def __init__(self, uid, name, parent, node):
        """
        Constructor

        :param uid: unique identifier for this object
        :type uid: int
        :param name: name identiying the sensor
        :type name: string
        :param carla_world: carla world object
        :type carla_world: carla.World
        :param parent: the parent of this
        :type parent: carla_ros_bridge.Parent
        :param node: node-handle
        :type node: carla_ros_bridge.CarlaRosBridge
        """

        super(TFSensor, self).__init__(uid,
                                       parent=parent,
                                       node=node,
                                       prefix=None)

        self.tf_broadcaster = tf.TransformBroadcaster()

    def update(self, frame, timestamp):
        """
        Function (override) to update this object.
        """
        pose = self.parent.get_current_ros_pose()
        position = pose.position
        orientation = pose.orientation
        self.tf_broadcaster.sendTransform(
            (position.x, position.y, position.z),
            (orientation.x, orientation.y, orientation.z, orientation.w),
            rospy.Time.now(), self.parent.get_prefix(), "map")