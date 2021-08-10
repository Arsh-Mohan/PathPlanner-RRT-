#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

# Simple talker demo that published std_msgs/Strings messages
# to the 'chatter' topic

import rospy
from std_msgs.msg import Float64MultiArray


def obs():
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('obs', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    pub = rospy.Publisher('chatter2', Float64MultiArray, queue_size=10)
    data_to_send = Float64MultiArray()  # the data to be sent, initialise the array
    '''data_to_send.data = [(0, 1.5, 0.25), (0, 3, 0.25), (0, 4.5, 0.25), (1.5, 0, 0.25), (3, 0, 0.25),
                    (4.5, 0, 0.25), (1.5, 1.5, 0.25), (1.5,3,0.25), (1.5,4.5,0.25),
                    (3,1.5,0.25), (3,3,0.25), (3,4.5,0.25), (4.5,1.5,0.25), (4.5,3,0.25),
                    (4.5,4.5,0.25)] # assign the array with the value you want to send'''
    # pub.publish(data_to_send)

    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        data_to_send.data = [(0, 1.5, 0.25), (0, 3, 0.25), (0, 4.5, 0.25), (1.5, 0, 0.25), (3, 0, 0.25),
                             (4.5, 0, 0.25), (1.5, 1.5, 0.25), (1.5,
                                                                3, 0.25), (1.5, 4.5, 0.25),
                             (3, 1.5, 0.25), (3, 3, 0.25), (3, 4.5,
                                                            0.25), (4.5, 1.5, 0.25), (4.5, 3, 0.25),
                             (4.5, 4.5, 0.25)]
        rospy.loginfo(data_to_send)
        pub.publish(data_to_send)
        rate.sleep()


if __name__ == '__main__':
    try:
        obs()
    except rospy.ROSInterruptException:
        pass
