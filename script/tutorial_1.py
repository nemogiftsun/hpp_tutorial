from hpp.corbaserver.pr2 import Robot
robot = Robot ('pr2')
robot.setJointBounds ("base_joint_x", [-4, -3])
robot.setJointBounds ("base_joint_y", [-5, -3])

from hpp_ros import ScenePublisher
r = ScenePublisher (robot)

from hpp.corbaserver import ProblemSolver
ps = ProblemSolver (robot)

q_init = [-3.2, -4, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
r (q_init)

q_goal = [-3.2, -4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.5, 0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
r (q_goal)

#ps.loadObstacleFromUrdf ("iai_maps", "kitchen_area")

ps.setInitialConfig (q_init)
ps.addGoalConfig (q_goal)
ps.solve ()

from hpp_ros import PathPlayer
pp = PathPlayer (robot.client, r)

pp (0)
pp (1)

 'l_gripper_l_parallel_root_joint', 'l_gripper_r_finger_joint', 'l_gripper_r_finger_tip_joint', 'l_gripper_joint', 'l_gripper_r_parallel_root_joint', 'laser_tilt_mount_joint', 'r_shoulder_pan_joint', 'r_shoulder_lift_joint', 'r_upper_arm_roll_joint', 'r_elbow_flex_joint', 'r_forearm_roll_joint', 'r_wrist_flex_joint', 'r_wrist_roll_joint', 'r_gripper_l_finger_joint', 'r_gripper_l_finger_tip_joint', 'r_gripper_l_parallel_root_joint', 'r_gripper_r_finger_joint', 'r_gripper_r_finger_tip_joint', 'r_gripper_joint', 'r_gripper_r_parallel_root_joint']


        - l_gripper_motor_slider_joint
        - l_gripper_motor_screw_joint

        - l_gripper_r_finger_joint
        - l_gripper_r_finger_tip_joint
        - l_gripper_joint
        - laser_tilt_mount_joint
        - r_shoulder_pan_joint
        - r_shoulder_lift_joint
        - r_upper_arm_roll_joint
        - r_elbow_flex_joint
        - r_forearm_roll_joint
        - r_wrist_flex_joint
        - r_wrist_roll_joint
        - r_gripper_l_finger_joint
        - r_gripper_l_finger_tip_joint
        - r_gripper_motor_slider_joint
        - r_gripper_motor_screw_joint
        - r_gripper_r_finger_joint
        - r_gripper_r_finger_tip_joint
        - r_gripper_joint
        - torso_lift_motor_screw_joint

