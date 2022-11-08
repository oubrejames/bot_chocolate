<<<<<<< HEAD
# import rclpy
# from rclpy.node import Node
# from rclpy.action import ActionServer
# from moveit_msgs.action import MoveGroup

# class Intercept(Node):
#     def __init__(self):
#         super().__init__("fake_movegroup")
#         self._action_server = ActionServer(
#             self, 
#             MoveGroup,
#             "move_action",
#             self.move_action_callback)
        
#     def move_action_callback(self, goal):
#         self.get_logger().info(f"{goal.request.request}")
#         result = MoveGroup.Result()
#         return result
    
# def main(args=None):
#     rclpy.init(args=args)
#     node = Intercept()
#     rclpy.spin(node)
#     rclpy.shutdown()
    
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from moveit_msgs.action import MoveGroup
=======

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from moveit_msgs.action import MoveGroup, ExecuteTrajectory
>>>>>>> ag
import moveit_msgs
import std_msgs
import builtin_interfaces.msg
import geometry_msgs
import octomap_msgs
import sensor_msgs
<<<<<<< HEAD
from moveit_msgs.msg import PositionIKRequest
=======
import trajectory_msgs
from moveit_msgs.msg import PositionIKRequest, MotionPlanRequest
>>>>>>> ag
from sensor_msgs.msg import JointState
from moveit_msgs.srv import GetPositionIK
from std_srvs.srv import Empty
from rclpy.callback_groups import ReentrantCallbackGroup


class Testing(Node):
    def __init__(self):
        super().__init__("fake_movegroup")
<<<<<<< HEAD
        self._action_client = ActionClient(
=======
        self.cbgroup = ReentrantCallbackGroup()
        self._plan_client = ActionClient(
>>>>>>> ag
            self, 
            MoveGroup,
            "move_action",)

<<<<<<< HEAD
        self.cbgroup = ReentrantCallbackGroup()
        self.jointpub  = self.create_subscription(JointState, "/joint_states",self.js_cb, 10)
        self.ik_client= self.create_client(GetPositionIK, "/compute_ik",callback_group=self.cbgroup)
        self.empty    = self.create_service(Empty,"toggle",self.toggle_callback,callback_group=self.cbgroup)
        self.time=0
        # self.joint_states=JointState()
=======
        self._execute_client = ActionClient(
            self, 
            ExecuteTrajectory,
            "execute_trajectory")


        self.jointpub  = self.create_subscription(JointState, "/joint_states",self.js_cb, 10)
        self.ik_client= self.create_client(GetPositionIK, "/compute_ik",callback_group=self.cbgroup)
        self.call_ik    = self.create_service(Empty,"call_ik",self.ik_callback,callback_group=self.cbgroup)
        self.call_plan    = self.create_service(Empty,"call_plan",self.plan_callback,callback_group=self.cbgroup)
        self.call_execute   = self.create_service(Empty,"call_execute",self.execute_callback,callback_group=self.cbgroup)
        self.time=0
>>>>>>> ag


    def js_cb(self, jointstate):
        """ 
        Callback function of the goal pose subscriber
        Stores the GoalPose message recieved 
         """
        self.joint_statesmsg=jointstate 
        # self.get_logger().info(f'goal msg {self.joint_statesmsg}')
    


    def get_ik(self):
        ikmsg = PositionIKRequest()
        ikmsg.group_name = 'panda_manipulator'
        ikmsg.robot_state.joint_state = self.joint_statesmsg
        print(self.joint_statesmsg)

        ikmsg.pose_stamped.header.frame_id = 'panda_link0'
        ikmsg.pose_stamped.header.stamp = self.get_clock().now().to_msg()
        ikmsg.pose_stamped.pose.position.x = 0.5
        ikmsg.pose_stamped.pose.position.y = 0.5
        ikmsg.pose_stamped.pose.position.z = 0.5
        ikmsg.pose_stamped.pose.orientation.x = 0.0
        ikmsg.pose_stamped.pose.orientation.y = 0.0
        ikmsg.pose_stamped.pose.orientation.z = 0.0
        ikmsg.pose_stamped.pose.orientation.w = 0.0
        ikmsg.timeout.sec = 5

        return ikmsg
        # self.ik_future = self.ik_client.call_async(GetPositionIK.Request(ik_request = ikmsg))

        # self.response=GetPositionIK.Response()
        # self.get_logger().info(f'response{self.response}')

<<<<<<< HEAD
    async def toggle_callback(self,request,response):
 
        msg=self.get_ik()
        
        await self.ik_client.call_async(GetPositionIK.Request(ik_request=msg))
        self.response=GetPositionIK.Response()
=======
    async def ik_callback(self,request,response):
 
        msg=self.get_ik()
        
        self.response=await self.ik_client.call_async(GetPositionIK.Request(ik_request=msg))
        # self.response=GetPositionIK.Response()
>>>>>>> ag
        self.get_logger().info(f'\nresponse\n{self.response}')

        response=Empty.Response()
        return response 

    
<<<<<<< HEAD

        

        

        
        
        
        
    # def send_goal(self):
    #     goalmsg=moveit_msgs.action.MoveGroup.Goal(
    #         request=moveit_msgs.msg.MotionPlanRequest(
    #         workspace_parameters=moveit_msgs.msg.WorkspaceParameters(
    #         header=std_msgs.msg.Header(
    #         stamp=self.get_clock().now().to_msg(),
    #         frame_id='panda_link0'),
    #         min_corner=geometry_msgs.msg.Vector3(
    #         x=-1.0,
    #         y=-1.0,
    #         z=-1.0),
    #         max_corner=geometry_msgs.msg.Vector3(
    #         x=1.0,
    #         y=1.0,
    #         z=1.0)),
    #         start_state=moveit_msgs.msg.RobotState(
    #         joint_state=sensor_msgs.msg.JointState(
    #         header=std_msgs.msg.Header(
    #         stamp=builtin_interfaces.msg.Time(
    #         sec=0,
    #         nanosec=0),
    #         frame_id='panda_link0'),
    #         name=['panda_joint1',
    #         'panda_joint2',
    #         'panda_joint3',
    #         'panda_joint4',
    #         'panda_joint5',
    #         'panda_joint6',
    #         'panda_joint7',
    #         'panda_finger_joint1',
    #         'panda_finger_joint2'],
    #         position=[-3.05743667552222e-05,
    #         0.45826129385071196,
    #         0.36520248871411476,
    #         -1.8763676740530548,
    #         -0.21278170570578495,
    #         2.2968262699790225,
    #         1.2581421343073955,
    #         0.035,
    #         0.035],
    #         velocity=[],
    #         effort=[]),
    #         multi_dof_joint_state=sensor_msgs.msg.MultiDOFJointState(
    #         header=std_msgs.msg.Header(
    #         stamp=builtin_interfaces.msg.Time(
    #         sec=0,
    #         nanosec=0),
    #         frame_id='panda_link0'),
    #         joint_names=[],
    #         transforms=[],
    #         twist=[],
    #         wrench=[]),
    #         attached_collision_objects=[],
    #         is_diff=False),
    #         goal_constraints=[moveit_msgs.msg.Constraints(
    #         name='',
    #         joint_constraints=[moveit_msgs.msg.JointConstraint(
    #         joint_name='panda_joint1',
    #         position=-0.799720847385826,
    #         tolerance_above=0.0001,
    #         tolerance_below=0.0001,
    #         weight=1.0),
    #         moveit_msgs.msg.JointConstraint(
    #         joint_name='panda_joint2',
    #         position=0.6631403268111388,
    #         tolerance_above=0.0001,
    #         tolerance_below=0.0001,
    #         weight=1.0),
    #         moveit_msgs.msg.JointConstraint(
    #         joint_name='panda_joint3',
    #         position=0.1428222590095236,
    #         tolerance_above=0.0001,
    #         tolerance_below=0.0001,
    #         weight=1.0),
    #         moveit_msgs.msg.JointConstraint(
    #         joint_name='panda_joint4',
    #         position=-1.9078958035320892,
    #         tolerance_above=0.0001,
    #         tolerance_below=0.0001,
    #         weight=1.0),
    #         moveit_msgs.msg.JointConstraint(
    #         joint_name='panda_joint5',
    #         position=-0.16023113114248438,
    #         tolerance_above=0.0001,
    #         tolerance_below=0.0001,
    #         weight=1.0),
    #         moveit_msgs.msg.JointConstraint(
    #         joint_name='panda_joint6',
    #         position=2.5601750273131985,
    #         tolerance_above=0.0001,
    #         tolerance_below=0.0001,
    #         weight=1.0),
    #         moveit_msgs.msg.JointConstraint(
    #         joint_name='panda_joint7',
    #         position=0.2327714355052132,
    #         tolerance_above=0.0001,
    #         tolerance_below=0.0001,
    #         weight=1.0)],
    #         position_constraints=[],
    #         orientation_constraints=[],
    #         visibility_constraints=[])],
    #         path_constraints=moveit_msgs.msg.Constraints(
    #         name='',
    #         joint_constraints=[],
    #         position_constraints=[],
    #         orientation_constraints=[],
    #         visibility_constraints=[]),
    #         trajectory_constraints=moveit_msgs.msg.TrajectoryConstraints(
    #         constraints=[]),
    #         reference_trajectories=[],
    #         pipeline_id='move_group',
    #         planner_id='',
    #         group_name='panda_manipulator',
    #         num_planning_attempts=10,
    #         allowed_planning_time=5.0,
    #         max_velocity_scaling_factor=0.1,
    #         max_acceleration_scaling_factor=0.1,
    #         cartesian_speed_end_effector_link='',
    #         max_cartesian_speed=0.0),
    #         planning_options=moveit_msgs.msg.PlanningOptions(
    #         planning_scene_diff=moveit_msgs.msg.PlanningScene(
    #         name='',
    #         robot_state=moveit_msgs.msg.RobotState(
    #         joint_state=sensor_msgs.msg.JointState(
    #         header=std_msgs.msg.Header(
    #         stamp=builtin_interfaces.msg.Time(
    #         sec=0,
    #         nanosec=0),
    #         frame_id=''),
    #         name=[],
    #         position=[],
    #         velocity=[],
    #         effort=[]),
    #         multi_dof_joint_state=sensor_msgs.msg.MultiDOFJointState(
    #         header=std_msgs.msg.Header(
    #         stamp=builtin_interfaces.msg.Time(
    #         sec=0,
    #         nanosec=0),
    #         frame_id=''),
    #         joint_names=[],
    #         transforms=[],
    #         twist=[],
    #         wrench=[]),
    #         attached_collision_objects=[],
    #         is_diff=True),
    #         robot_model_name='',
    #         fixed_frame_transforms=[],
    #         allowed_collision_matrix=moveit_msgs.msg.AllowedCollisionMatrix(
    #         entry_names=[],
    #         entry_values=[],
    #         default_entry_names=[],
    #         default_entry_values=[]),
    #         link_padding=[],
    #         link_scale=[],
    #         object_colors=[],
    #         world=moveit_msgs.msg.PlanningSceneWorld(
    #         collision_objects=[],
    #         octomap=octomap_msgs.msg.OctomapWithPose(
    #         header=std_msgs.msg.Header(
    #         stamp=builtin_interfaces.msg.Time(
    #         sec=0,
    #         nanosec=0),
    #         frame_id=''),
    #         origin=geometry_msgs.msg.Pose(
    #         position=geometry_msgs.msg.Point(
    #         x=0.0,
    #         y=0.0,
    #         z=0.0),
    #         orientation=geometry_msgs.msg.Quaternion(
    #         x=0.0,
    #         y=0.0,
    #         z=0.0,
    #         w=1.0)),
    #         octomap=octomap_msgs.msg.Octomap(
    #         header=std_msgs.msg.Header(
    #         stamp=builtin_interfaces.msg.Time(
    #         sec=0,
    #         nanosec=0),
    #         frame_id=''),
    #         binary=False,
    #         id='',
    #         resolution=0.0,
    #         data=[]))),
    #         is_diff=True),
    #         plan_only=True,
    #         look_around=False,
    #         look_around_attempts=0,
    #         max_safe_execution_cost=0.0,
    #         replan=False,
    #         replan_attempts=0,
    #         replan_delay=0.0))

    #     self._action_client.wait_for_server()
    #     return self._action_client.send_goal_async(goalmsg)
=======
    def send_plan(self):
        plan_request=moveit_msgs.action.MoveGroup.Goal(
            request=moveit_msgs.msg.MotionPlanRequest(
            workspace_parameters=moveit_msgs.msg.WorkspaceParameters(
            header=std_msgs.msg.Header(
            stamp=self.get_clock().now().to_msg(),
            frame_id='panda_link0'),
            min_corner=geometry_msgs.msg.Vector3(
            x=-1.0,
            y=-1.0,
            z=-1.0),
            max_corner=geometry_msgs.msg.Vector3(
            x=1.0,
            y=1.0,
            z=1.0)),
            start_state=moveit_msgs.msg.RobotState(
            joint_state=sensor_msgs.msg.JointState(
            header=std_msgs.msg.Header(
            stamp=builtin_interfaces.msg.Time(
            sec=0,
            nanosec=0),
            frame_id='panda_link0'),
            name=['panda_joint1',
            'panda_joint2',
            'panda_joint3',
            'panda_joint4',
            'panda_joint5',
            'panda_joint6',
            'panda_joint7',
            'panda_finger_joint1',
            'panda_finger_joint2'],
            position=[-3.05743667552222e-05,
            0.45826129385071196,
            0.36520248871411476,
            -1.8763676740530548,
            -0.21278170570578495,
            2.2968262699790225,
            1.2581421343073955,
            0.035,
            0.035],
            velocity=[],
            effort=[]),
            multi_dof_joint_state=sensor_msgs.msg.MultiDOFJointState(
            header=std_msgs.msg.Header(
            stamp=builtin_interfaces.msg.Time(
            sec=0,
            nanosec=0),
            frame_id='panda_link0'),
            joint_names=[],
            transforms=[],
            twist=[],
            wrench=[]),
            attached_collision_objects=[],
            is_diff=False),
            goal_constraints=[moveit_msgs.msg.Constraints(
            name='',
            joint_constraints=[moveit_msgs.msg.JointConstraint(
            joint_name='panda_joint1',
            position=-0.799720847385826,
            tolerance_above=0.0001,
            tolerance_below=0.0001,
            weight=1.0),
            moveit_msgs.msg.JointConstraint(
            joint_name='panda_joint2',
            position=0.6631403268111388,
            tolerance_above=0.0001,
            tolerance_below=0.0001,
            weight=1.0),
            moveit_msgs.msg.JointConstraint(
            joint_name='panda_joint3',
            position=0.1428222590095236,
            tolerance_above=0.0001,
            tolerance_below=0.0001,
            weight=1.0),
            moveit_msgs.msg.JointConstraint(
            joint_name='panda_joint4',
            position=-1.9078958035320892,
            tolerance_above=0.0001,
            tolerance_below=0.0001,
            weight=1.0),
            moveit_msgs.msg.JointConstraint(
            joint_name='panda_joint5',
            position=-0.16023113114248438,
            tolerance_above=0.0001,
            tolerance_below=0.0001,
            weight=1.0),
            moveit_msgs.msg.JointConstraint(
            joint_name='panda_joint6',
            position=2.5601750273131985,
            tolerance_above=0.0001,
            tolerance_below=0.0001,
            weight=1.0),
            moveit_msgs.msg.JointConstraint(
            joint_name='panda_joint7',
            position=0.2327714355052132,
            tolerance_above=0.0001,
            tolerance_below=0.0001,
            weight=1.0)],
            position_constraints=[],
            orientation_constraints=[],
            visibility_constraints=[])],
            path_constraints=moveit_msgs.msg.Constraints(
            name='',
            joint_constraints=[],
            position_constraints=[],
            orientation_constraints=[],
            visibility_constraints=[]),
            trajectory_constraints=moveit_msgs.msg.TrajectoryConstraints(
            constraints=[]),
            reference_trajectories=[],
            pipeline_id='move_group',
            planner_id='',
            group_name='panda_manipulator',
            num_planning_attempts=10,
            allowed_planning_time=5.0,
            max_velocity_scaling_factor=0.1,
            max_acceleration_scaling_factor=0.1,
            cartesian_speed_end_effector_link='',
            max_cartesian_speed=0.0),
            planning_options=moveit_msgs.msg.PlanningOptions(
            planning_scene_diff=moveit_msgs.msg.PlanningScene(
            name='',
            robot_state=moveit_msgs.msg.RobotState(
            joint_state=sensor_msgs.msg.JointState(
            header=std_msgs.msg.Header(
            stamp=builtin_interfaces.msg.Time(
            sec=0,
            nanosec=0),
            frame_id=''),
            name=[],
            position=[],
            velocity=[],
            effort=[]),
            multi_dof_joint_state=sensor_msgs.msg.MultiDOFJointState(
            header=std_msgs.msg.Header(
            stamp=builtin_interfaces.msg.Time(
            sec=0,
            nanosec=0),
            frame_id=''),
            joint_names=[],
            transforms=[],
            twist=[],
            wrench=[]),
            attached_collision_objects=[],
            is_diff=True),
            robot_model_name='',
            fixed_frame_transforms=[],
            allowed_collision_matrix=moveit_msgs.msg.AllowedCollisionMatrix(
            entry_names=[],
            entry_values=[],
            default_entry_names=[],
            default_entry_values=[]),
            link_padding=[],
            link_scale=[],
            object_colors=[],
            world=moveit_msgs.msg.PlanningSceneWorld(
            collision_objects=[],
            octomap=octomap_msgs.msg.OctomapWithPose(
            header=std_msgs.msg.Header(
            stamp=builtin_interfaces.msg.Time(
            sec=0,
            nanosec=0),
            frame_id=''),
            origin=geometry_msgs.msg.Pose(
            position=geometry_msgs.msg.Point(
            x=0.0,
            y=0.0,
            z=0.0),
            orientation=geometry_msgs.msg.Quaternion(
            x=0.0,
            y=0.0,
            z=0.0,
            w=1.0)),
            octomap=octomap_msgs.msg.Octomap(
            header=std_msgs.msg.Header(
            stamp=builtin_interfaces.msg.Time(
            sec=0,
            nanosec=0),
            frame_id=''),
            binary=False,
            id='',
            resolution=0.0,
            data=[]))),
            is_diff=True),
            plan_only=True,
            look_around=False,
            look_around_attempts=0,
            max_safe_execution_cost=0.0,
            replan=False,
            replan_attempts=0,
            replan_delay=0.0))

        return plan_request



    async def plan_callback(self,request,response):
 
        plan_msg=self.send_plan()
        self.future_response=await self._plan_client.send_goal_async(plan_msg)
        # self.response=GetPositionIK.Response()
        self.response=await self.future_response.get_result_async()
        self.get_logger().info(f'\nresponse\n{self.response}')

        response=Empty.Response()
        return response 


    def send_execute(self):
        execute_msg=moveit_msgs.action.ExecuteTrajectory.Goal(
                    trajectory=moveit_msgs.msg.RobotTrajectory(
                    joint_trajectory=trajectory_msgs.msg.JointTrajectory(
                    header=std_msgs.msg.Header(
                    stamp=builtin_interfaces.msg.Time(
                    sec=0,
                    nanosec=0),
                    frame_id='panda_link0'),
                    joint_names=['panda_joint1',
                    'panda_joint2',
                    'panda_joint3',
                    'panda_joint4',
                    'panda_joint5',
                    'panda_joint6',
                    'panda_joint7'],
                    points=[trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[0.0,
                    -0.7853981633974483,
                    0.0,
                    -2.356194490192345,
                    0.0,
                    1.5707963267948966,
                    0.7853981633974483],
                    velocities=[-0.0,
                    0.0,
                    -0.0,
                    0.0,
                    -0.0,
                    0.0,
                    -0.0],
                    accelerations=[0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=0,
                    nanosec=0)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.0013285879594506157,
                    -0.7815948080091599,
                    -0.0039083082553501335,
                    -2.3554203009364887,
                    -0.00041377247539470317,
                    1.5739459117872223,
                    0.7803981633974483],
                    velocities=[-0.026571759189012435,
                    0.07606710776576718,
                    -0.07816616510700304,
                    0.01548378511712603,
                    -0.0082754495078941,
                    0.06299169984651574,
                    -0.10000000000000041],
                    accelerations=[-0.2657175918902132,
                    0.7606710776579261,
                    -0.781661651070299,
                    0.1548378511713117,
                    -0.08275449507896931,
                    0.6299169984653669,
                    -1.000000000000333],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=0,
                    nanosec=100000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.0053143518378024664,
                    -0.7701847418442949,
                    -0.015633233021400544,
                    -2.3530977331689193,
                    -0.0016550899015788138,
                    1.5833946667641996,
                    0.7653981633974483],
                    velocities=[-0.05314351837802419,
                    0.1521342155315324,
                    -0.15633233021400406,
                    0.03096757023425166,
                    -0.01655089901578799,
                    0.12598339969302988,
                    -0.19999999999999826],
                    accelerations=[-0.26571759188962124,
                    0.760671077656227,
                    -0.781661651068546,
                    0.15483785117096552,
                    -0.08275449507878538,
                    0.6299169984639621,
                    -0.9999999999981126],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=0,
                    nanosec=200000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.011755213406423156,
                    -0.7517464552574116,
                    -0.0345803206125126,
                    -2.3493445410754537,
                    -0.0036610174850448107,
                    1.5986635398484959,
                    0.7411586633974481],
                    velocities=[-0.06935229148332485,
                    0.1985351512686592,
                    -0.20401369092928498,
                    0.040412679155700335,
                    -0.021598923215604353,
                    0.1644083365994118,
                    -0.2610000000000101],
                    accelerations=[-2.8887016745572893e-12,
                    8.261986136557635e-12,
                    -8.501463995588292e-12,
                    1.6838286963093006e-12,
                    -9.017838129123144e-13,
                    6.855053714752531e-12,
                    -1.0896242585894853e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=0,
                    nanosec=300000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.01869044255475551,
                    -0.7318929401305462,
                    -0.05498168970544072,
                    -2.345303273159884,
                    -0.005820909806605205,
                    1.615104373508437,
                    0.7150586633974476],
                    velocities=[-0.0693522914833243,
                    0.19853515126865762,
                    -0.20401369092928334,
                    0.04041267915570001,
                    -0.02159892321560418,
                    0.16440833659941048,
                    -0.261000000000008],
                    accelerations=[-2.8863630235863535e-12,
                    8.262921596933482e-12,
                    -8.489303010548098e-12,
                    1.6789954843084016e-12,
                    -9.008093750081593e-13,
                    6.86690287964335e-12,
                    -1.0866307853501565e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=0,
                    nanosec=400000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.025625671703087875,
                    -0.7120394250036806,
                    -0.07538305879836886,
                    -2.341262005244314,
                    -0.007980802128165602,
                    1.6315452071683776,
                    0.6889586633974469],
                    velocities=[-0.06935229148331826,
                    0.1985351512686403,
                    -0.20401369092926555,
                    0.04041267915569521,
                    -0.021598923215602295,
                    0.1644083365993955,
                    -0.26099999999998524],
                    accelerations=[4.6648908311307275e-12,
                    -1.3318840252839675e-11,
                    1.3714449369260655e-11,
                    -2.711570818802137e-12,
                    1.4505667602102616e-12,
                    -1.1044087833419038e-11,
                    1.75386708279968e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=0,
                    nanosec=500000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.032560900851420244,
                    -0.6921859098768149,
                    -0.09578442789129701,
                    -2.337220737328744,
                    -0.010140694449726002,
                    1.6479860408283185,
                    0.6628586633974465],
                    velocities=[-0.06935229148332415,
                    0.19853515126865715,
                    -0.2040136909292829,
                    0.040412679155698635,
                    -0.02159892321560413,
                    0.16440833659940945,
                    -0.26100000000000745],
                    accelerations=[-3.0301862497614152e-12,
                    8.663771953543203e-12,
                    -8.919844030987829e-12,
                    1.7604955324318083e-12,
                    -9.442657855770607e-13,
                    7.1700181684495466e-12,
                    -1.143788612585999e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=0,
                    nanosec=600000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.03949612999975262,
                    -0.6723323947499494,
                    -0.11618579698422518,
                    -2.3331794694131744,
                    -0.012300586771286403,
                    1.6644268744882593,
                    0.6367586633974459],
                    velocities=[-0.06935229148332357,
                    0.19853515126865548,
                    -0.20401369092928118,
                    0.040412679155698294,
                    -0.02159892321560395,
                    0.16440833659940807,
                    -0.26100000000000523],
                    accelerations=[-3.0250166622764682e-12,
                    8.651547654110699e-12,
                    -8.893548987092817e-12,
                    1.7545096641203515e-12,
                    -9.453177069613963e-13,
                    7.139039322972465e-12,
                    -1.1374062650159521e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=0,
                    nanosec=700000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.046431359148084606,
                    -0.6524788796230849,
                    -0.1365871660771522,
                    -2.3291382014976048,
                    -0.014460479092846682,
                    1.6808677081481993,
                    0.6106586633974467],
                    velocities=[-0.0693522914833206,
                    0.198535151268647,
                    -0.20401369092927243,
                    0.04041267915569657,
                    -0.021598923215603024,
                    0.16440833659940104,
                    -0.26099999999999407],
                    accelerations=[5.920991423867257e-12,
                    -1.6931957931409876e-11,
                    1.745134314402981e-11,
                    -3.4539116639225664e-12,
                    1.8438175048007688e-12,
                    -1.402340074073824e-11,
                    2.222968710013321e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=0,
                    nanosec=800000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.05336658829641652,
                    -0.6326253644962206,
                    -0.15698853517007905,
                    -2.325096933582035,
                    -0.01662037141440694,
                    1.6973085418081393,
                    0.5845586633974479],
                    velocities=[-0.06935229148332149,
                    0.19853515126864957,
                    -0.20401369092927513,
                    0.04041267915569837,
                    -0.021598923215603305,
                    0.16440833659940382,
                    -0.2609999999999972],
                    accelerations=[6.116782544055741e-12,
                    -1.767070512727214e-11,
                    1.8123800130535528e-11,
                    -3.6247600261071057e-12,
                    1.9256537638694e-12,
                    -1.4725587606060115e-11,
                    2.31078451664328e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=0,
                    nanosec=900000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.06030181744474844,
                    -0.6127718493693564,
                    -0.17738990426300588,
                    -2.3210556656664654,
                    -0.0187802637359672,
                    1.7137493754680788,
                    0.5584586633974491],
                    velocities=[-0.06935229148331651,
                    0.19853515126863533,
                    -0.20401369092926047,
                    0.04041267915569547,
                    -0.021598923215601754,
                    0.16440833659939202,
                    -0.2609999999999784],
                    accelerations=[6.144034992018905e-12,
                    -1.7584138887569844e-11,
                    1.808994322105324e-11,
                    -3.5852601285146634e-12,
                    1.9153619981172735e-12,
                    -1.4579066082756722e-11,
                    2.3147986555887204e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=1,
                    nanosec=0)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.06723704659308112,
                    -0.5929183342424899,
                    -0.19779127335593497,
                    -2.3170143977508952,
                    -0.020940156057527692,
                    1.7301902091280206,
                    0.5323586633974473],
                    velocities=[-0.06935229148332908,
                    0.19853515126867127,
                    -0.20401369092929744,
                    0.04041267915570279,
                    -0.021598923215605668,
                    0.1644083365994218,
                    -0.2610000000000257],
                    accelerations=[-9.229525145831955e-12,
                    2.635937404732534e-11,
                    -2.7108219900942537e-11,
                    5.363608426533175e-12,
                    -2.8690156766708864e-12,
                    2.1828856632941298e-11,
                    -3.467156302247623e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=1,
                    nanosec=100000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.0741722757414138,
                    -0.5730648191156233,
                    -0.21819264244886402,
                    -2.3129731298353247,
                    -0.02310004837908819,
                    1.746631042787962,
                    0.5062586633974455],
                    velocities=[-0.06935229148332774,
                    0.19853515126866772,
                    -0.20401369092929336,
                    0.04041267915570201,
                    -0.021598923215605245,
                    0.16440833659941795,
                    -0.2610000000000212],
                    accelerations=[-9.444019252842763e-12,
                    2.70294344133086e-11,
                    -2.7773790610576993e-11,
                    5.512888086019051e-12,
                    -2.9425330923266245e-12,
                    2.237720818038113e-11,
                    -3.5543008419565864e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=1,
                    nanosec=200000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.08110750488974647,
                    -0.5532113039887568,
                    -0.23859401154179308,
                    -2.308931861919755,
                    -0.025259940700648686,
                    1.7630718764479036,
                    0.4801586633974438],
                    velocities=[-0.06935229148332075,
                    0.19853515126864774,
                    -0.20401369092927285,
                    0.04041267915569794,
                    -0.021598923215603073,
                    0.1644083365994014,
                    -0.26099999999999496],
                    accelerations=[3.3235074081312435e-12,
                    -9.525103705778203e-12,
                    9.730681483600754e-12,
                    -1.918725926343811e-12,
                    1.0278888891127558e-12,
                    -7.880481483197795e-12,
                    1.247171852123477e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=1,
                    nanosec=300000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.08804273403807852,
                    -0.5333577888618921,
                    -0.2589953806347203,
                    -2.304890594004185,
                    -0.027419833022208982,
                    1.7795127101078436,
                    0.4540586633974444],
                    velocities=[-0.0693522914833214,
                    0.19853515126864957,
                    -0.2040136909292747,
                    0.040412679155698315,
                    -0.02159892321560327,
                    0.16440833659940293,
                    -0.26099999999999735],
                    accelerations=[3.315585815901867e-12,
                    -9.491677041601423e-12,
                    9.751722987946668e-12,
                    -1.8853331110030226e-12,
                    1.0239309137344002e-12,
                    -7.801378390357335e-12,
                    1.2482205424571735e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=1,
                    nanosec=400000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.09497796318641057,
                    -0.5135042737350275,
                    -0.2793967497276474,
                    -2.3008493260886156,
                    -0.029579725343769278,
                    1.7959535437677838,
                    0.4279586633974451],
                    velocities=[-0.06935229148332202,
                    0.19853515126865137,
                    -0.20401369092927657,
                    0.040412679155698676,
                    -0.021598923215603468,
                    0.1644083365994044,
                    -0.26099999999999973],
                    accelerations=[3.8028588907723745e-12,
                    -1.0140957042059667e-11,
                    1.0140957042059667e-11,
                    -1.9014294453861873e-12,
                    9.507147226930936e-13,
                    -8.873337411802208e-12,
                    1.2676196302574583e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=1,
                    nanosec=500000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.10191319233474262,
                    -0.49365075860816277,
                    -0.2997981188205747,
                    -2.2968080581730455,
                    -0.03173961766532958,
                    1.812394377427724,
                    0.4018586633974457],
                    velocities=[-0.0693522914833191,
                    0.19853515126864282,
                    -0.2040136909292682,
                    0.040412679155697,
                    -0.02159892321560257,
                    0.16440833659939824,
                    -0.2609999999999884],
                    accelerations=[3.5044497181872414e-12,
                    -1.0008203249237436e-11,
                    1.0292347820982348e-11,
                    -2.036369430838532e-12,
                    1.089220858355494e-12,
                    -8.303335818767968e-12,
                    1.3196936776596998e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=1,
                    nanosec=600000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.10884842148307466,
                    -0.47379724348129815,
                    -0.3201994879135019,
                    -2.2927667902574758,
                    -0.03389950998688988,
                    1.828835211087664,
                    0.37575866339744635],
                    velocities=[-0.06935229148331977,
                    0.1985351512686447,
                    -0.20401369092927016,
                    0.040412679155697386,
                    -0.021598923215602778,
                    0.16440833659939982,
                    -0.2609999999999909],
                    accelerations=[3.5120369953914718e-12,
                    -1.005169209025835e-11,
                    1.0293901538216383e-11,
                    -2.0385961869801073e-12,
                    1.0899425158111464e-12,
                    -8.315857713225784e-12,
                    1.3240783155039112e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=1,
                    nanosec=700000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.11578365063140669,
                    -0.45394372835443353,
                    -0.34060085700642906,
                    -2.288725522341906,
                    -0.03605940230845017,
                    1.8452760447476042,
                    0.349658663397447],
                    velocities=[-0.06935229148332045,
                    0.19853515126864665,
                    -0.20401369092927213,
                    0.04041267915569778,
                    -0.02159892321560299,
                    0.1644083365994014,
                    -0.26099999999999346],
                    accelerations=[3.4975052554220185e-12,
                    -1.001685505152866e-11,
                    1.0296655471962422e-11,
                    -2.028553048144771e-12,
                    1.0842266291808257e-12,
                    -8.338052528926091e-12,
                    1.3206579844473542e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=1,
                    nanosec=800000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.12271887977973873,
                    -0.4340902132275688,
                    -0.3610022260993563,
                    -2.284684254426336,
                    -0.038219294630010475,
                    1.8617168784075444,
                    0.32355866339744765],
                    velocities=[-0.069352291483321,
                    0.19853515126864812,
                    -0.20401369092927363,
                    0.0404126791556968,
                    -0.02159892321560315,
                    0.16440833659940263,
                    -0.2609999999999954],
                    accelerations=[3.4762824502934633e-12,
                    -9.954808834931282e-12,
                    1.0270834512230687e-11,
                    -2.0344152976149247e-12,
                    1.0764624633011008e-12,
                    -8.295674029109402e-12,
                    1.3115065607925339e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=1,
                    nanosec=900000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.12965410892807078,
                    -0.4142366981007042,
                    -0.3814035951922835,
                    -2.2806429865107667,
                    -0.04037918695157077,
                    1.8781577120674848,
                    0.2974586633974483],
                    velocities=[-0.06935229148332167,
                    0.19853515126865004,
                    -0.2040136909292756,
                    0.04041267915569719,
                    -0.021598923215603354,
                    0.1644083365994042,
                    -0.2609999999999979],
                    accelerations=[3.4751598401487985e-12,
                    -9.904205544424076e-12,
                    1.0251721528438956e-11,
                    -2.041656406087419e-12,
                    1.0859874500464995e-12,
                    -8.340383616357116e-12,
                    1.3205607392565434e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=2,
                    nanosec=0)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.13658933807640283,
                    -0.3943831829738395,
                    -0.40180496428521073,
                    -2.276601718595197,
                    -0.04253907927313107,
                    1.8945985457274246,
                    0.27135866339744896],
                    velocities=[-0.06935229148331884,
                    0.19853515126864194,
                    -0.20401369092926727,
                    0.04041267915569555,
                    -0.021598923215602476,
                    0.16440833659939752,
                    -0.2609999999999873],
                    accelerations=[3.4906130847365184e-12,
                    -9.985442348959384e-12,
                    1.0271558175577132e-11,
                    -2.0314223689860068e-12,
                    1.0836636933147184e-12,
                    -8.268747389252901e-12,
                    1.3104104859092831e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=2,
                    nanosec=100000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.14352456722473492,
                    -0.37452966784697483,
                    -0.42220633337813795,
                    -2.2725604506796273,
                    -0.04469897159469138,
                    1.9110393793873648,
                    0.2452586633974496],
                    velocities=[-0.06935229148331952,
                    0.19853515126864388,
                    -0.20401369092926927,
                    0.040412679155695935,
                    -0.021598923215602684,
                    0.1644083365993991,
                    -0.26099999999998985],
                    accelerations=[3.476083066454421e-12,
                    -9.946945390161882e-12,
                    1.0232162462281218e-11,
                    -2.032171638850277e-12,
                    1.082933570703108e-12,
                    -8.271295091460776e-12,
                    1.3048681049459672e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=2,
                    nanosec=200000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.15045979637306695,
                    -0.35467615272011005,
                    -0.4426077024710652,
                    -2.2685191827640576,
                    -0.04685886391625168,
                    1.9274802130473048,
                    0.21915866339745013],
                    velocities=[-0.06935229148331996,
                    0.19853515126864538,
                    -0.20401369092927066,
                    0.040412679155697524,
                    -0.021598923215602847,
                    0.1644083365993997,
                    -0.26099999999999196],
                    accelerations=[3.39374476189917e-12,
                    -9.677646353286666e-12,
                    9.94038788324015e-12,
                    -1.970561474651131e-12,
                    1.0564399016879675e-12,
                    -8.013616663581266e-12,
                    1.2699173947751733e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=2,
                    nanosec=300000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.157395025521399,
                    -0.3348226375932454,
                    -0.4630090715639925,
                    -2.264477914848488,
                    -0.04901875623781198,
                    1.9439210467072452,
                    0.1930586633974507],
                    velocities=[-0.06935229148332062,
                    0.19853515126864724,
                    -0.20401369092927257,
                    0.0404126791556979,
                    -0.02159892321560305,
                    0.16440833659940124,
                    -0.2609999999999944],
                    accelerations=[3.3889662229469536e-12,
                    -9.664829598774647e-12,
                    9.915864133807754e-12,
                    -1.976896963385723e-12,
                    1.059051944670923e-12,
                    -8.033105121059446e-12,
                    1.2677244019171939e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=2,
                    nanosec=400000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.16433025466973145,
                    -0.3149691224663796,
                    -0.4834104406569208,
                    -2.260436646932918,
                    -0.05117864855937241,
                    1.960361880367186,
                    0.16695866339744986],
                    velocities=[-0.06935229148332767,
                    0.19853515126866741,
                    -0.20401369092929328,
                    0.04041267915570201,
                    -0.021598923215605245,
                    0.16440833659941795,
                    -0.2610000000000209],
                    accelerations=[-2.214350398042394e-11,
                    6.344113890391459e-11,
                    -6.510190170244638e-11,
                    1.2898591068596946e-11,
                    -6.892165613906952e-12,
                    5.248010443360474e-11,
                    -8.325957496639402e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=2,
                    nanosec=500000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.1712654838180648,
                    -0.29511560733951125,
                    -0.5038118097498517,
                    -2.2563953790173477,
                    -0.0533385408809331,
                    1.9768027140271294,
                    0.1408586633974457],
                    velocities=[-0.06935229148332453,
                    0.1985351512686583,
                    -0.2040136909292838,
                    0.040412679155700085,
                    -0.021598923215604224,
                    0.16440833659941018,
                    -0.2610000000000089],
                    accelerations=[-2.2255309285143328e-11,
                    6.362400183870387e-11,
                    -6.545679201512744e-11,
                    1.2894988026980105e-11,
                    -6.938419953603508e-12,
                    5.288908794822297e-11,
                    -8.378469377936312e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=2,
                    nanosec=600000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.1782007129663981,
                    -0.2752620922126429,
                    -0.5242131788427827,
                    -2.2523541111017766,
                    -0.05549843320249379,
                    1.9932435476870722,
                    0.11475866339744153],
                    velocities=[-0.06935229148334252,
                    0.1985351512687098,
                    -0.2040136909293367,
                    0.04041267915571057,
                    -0.021598923215609824,
                    0.1644083365994528,
                    -0.26100000000007656],
                    accelerations=[-2.2201987238881982e-11,
                    6.354675201524475e-11,
                    -6.530352590317811e-11,
                    1.2933490519785274e-11,
                    -6.91351103311707e-12,
                    5.264263822807215e-11,
                    -8.353762729172783e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=2,
                    nanosec=700000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.18513594211473147,
                    -0.25540857708577447,
                    -0.5446145479357138,
                    -2.248312843186206,
                    -0.0576583255240545,
                    2.0096843813470153,
                    0.08865866339743722],
                    velocities=[-0.06935229148333827,
                    0.1985351512686976,
                    -0.20401369092932417,
                    0.040412679155708085,
                    -0.0215989232156085,
                    0.1644083365994427,
                    -0.2610000000000605],
                    accelerations=[-2.2211164064228558e-11,
                    6.353158824578479e-11,
                    -6.529316332674085e-11,
                    1.2924599778753687e-11,
                    -6.9122674372297496e-12,
                    5.261748176594834e-11,
                    -8.348334079313493e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=2,
                    nanosec=800000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.19207117126306478,
                    -0.2355550619589062,
                    -0.5650159170286447,
                    -2.244271575270636,
                    -0.059818217845615196,
                    2.0261252150069584,
                    0.06255866339743305],
                    velocities=[-0.06935229148333401,
                    0.19853515126868543,
                    -0.20401369092931165,
                    0.04041267915570561,
                    -0.021598923215607174,
                    0.16440833659943263,
                    -0.26100000000004453],
                    accelerations=[-2.2200908101692246e-11,
                    6.350552845032717e-11,
                    -6.52753546530412e-11,
                    1.2922333965404689e-11,
                    -6.910130247361419e-12,
                    5.2626302674820304e-11,
                    -8.349415379862687e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=2,
                    nanosec=900000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.19900640041139803,
                    -0.215701546832038,
                    -0.5854172861215755,
                    -2.2402303073550653,
                    -0.06197811016717587,
                    2.0425660486669015,
                    0.03645866339742912],
                    velocities=[-0.06935229148333068,
                    0.19853515126867607,
                    -0.2040136909293025,
                    0.040412679155702486,
                    -0.021598923215606188,
                    0.1644083365994264,
                    -0.261000000000032],
                    accelerations=[-2.1895601894784718e-11,
                    6.265071080497943e-11,
                    -6.436521144274398e-11,
                    1.2751598493373807e-11,
                    -6.8133540969497305e-12,
                    5.18636442923775e-11,
                    -8.229603061269818e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=3,
                    nanosec=0)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.2059416295597314,
                    -0.1958480317051696,
                    -0.6058186552145066,
                    -2.2361890394394948,
                    -0.06413800248873658,
                    2.059006882326845,
                    0.010358663397424871],
                    velocities=[-0.06935229148332649,
                    0.19853515126866408,
                    -0.20401369092929017,
                    0.04041267915570004,
                    -0.02159892321560488,
                    0.16440833659941648,
                    -0.2610000000000162],
                    accelerations=[-2.191320881112885e-11,
                    6.270982585821439e-11,
                    -6.44008773420314e-11,
                    1.2753346607120005e-11,
                    -6.799436174514256e-12,
                    5.1858912170388525e-11,
                    -8.229783887909484e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=3,
                    nanosec=100000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.2128768587080647,
                    -0.17599451657830129,
                    -0.6262200243074375,
                    -2.2321477715239246,
                    -0.06629789481029727,
                    2.075447715986788,
                    -0.01574133660257923],
                    velocities=[-0.0693522914833223,
                    0.19853515126865207,
                    -0.20401369092927785,
                    0.0404126791556976,
                    -0.021598923215603576,
                    0.16440833659940654,
                    -0.26100000000000045],
                    accelerations=[-2.318294340691892e-11,
                    6.182118241845045e-11,
                    -6.697294761998799e-11,
                    1.2879413003843844e-11,
                    -6.439706501921922e-12,
                    5.1517652015375377e-11,
                    -8.24282432246006e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=3,
                    nanosec=200000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.21981208785639803,
                    -0.15614100145143306,
                    -0.6466213934003684,
                    -2.228106503608354,
                    -0.06845778713185796,
                    2.091888549646731,
                    -0.04184133660258331],
                    velocities=[-0.06935229148334128,
                    0.1985351512687062,
                    -0.20401369092933316,
                    0.0404126791557099,
                    -0.021598923215609467,
                    0.1644083365994501,
                    -0.26100000000007206],
                    accelerations=[-2.21852235684706e-11,
                    6.354723212143501e-11,
                    -6.531690187671547e-11,
                    1.2934677120413605e-11,
                    -6.913777975743467e-12,
                    5.260745545242847e-11,
                    -8.352841244923812e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=3,
                    nanosec=300000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.22674731700473133,
                    -0.13628748632456472,
                    -0.6670227624932994,
                    -2.224065235692783,
                    -0.07061767945341865,
                    2.1083293833066743,
                    -0.06794133660258747],
                    velocities=[-0.06935229148333703,
                    0.19853515126869403,
                    -0.20401369092932065,
                    0.040412679155707426,
                    -0.021598923215608145,
                    0.16440833659944,
                    -0.2610000000000561],
                    accelerations=[-2.219034949321043e-11,
                    6.357235260217042e-11,
                    -6.530952814497534e-11,
                    1.2935753595529472e-11,
                    -6.917681179383866e-12,
                    5.261160215352035e-11,
                    -8.354987134442696e-11],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=3,
                    nanosec=400000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.23353039857118296,
                    -0.11686952484038035,
                    -0.6869765589237884,
                    -2.2201126265840005,
                    -0.07273018727090291,
                    2.124409531972369,
                    -0.09346874530067817],
                    velocities=[-0.06036026289468412,
                    0.17279362610957857,
                    -0.17756183328949315,
                    0.035172881615643595,
                    -0.018798465856740172,
                    0.14309160096900686,
                    -0.22715945325759118],
                    accelerations=[0.26571759189700506,
                    -0.7606710776773843,
                    0.7816616510903032,
                    -0.1548378511752717,
                    0.08275449508108579,
                    -0.6299169984814715,
                    1.0000000000259213],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=3,
                    nanosec=500000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.2382378369012013,
                    -0.10339351761770929,
                    -0.700824433997389,
                    -2.2173695276782923,
                    -0.07419626138118239,
                    2.135569107076945,
                    -0.11118469062643932],
                    velocities=[-0.033788503705687235,
                    0.09672651834385593,
                    -0.09939566818253592,
                    0.01968909649852663,
                    -0.010523016348850915,
                    0.08009990112252822,
                    -0.12715945325764924],
                    accelerations=[0.26571759187884364,
                    -0.7606710776253878,
                    0.7816616510368594,
                    -0.15483785116469118,
                    0.08275449507542966,
                    -0.6299169984384175,
                    0.9999999999575682],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=3,
                    nanosec=600000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.24028809931231848,
                    -0.09752422117161474,
                    -0.7068556925602898,
                    -2.2161748072842964,
                    -0.07483479054067248,
                    2.14042951219687,
                    -0.1189006359522007],
                    velocities=[-0.007216744516663792,
                    0.020659410578057265,
                    -0.021229503075500582,
                    0.004205311381394191,
                    -0.0022475668409533875,
                    0.017108201275986636,
                    -0.027159453257607376],
                    accelerations=[0.26571759189187033,
                    -0.760671077662671,
                    0.7816616510751633,
                    -0.1548378511722774,
                    0.08275449507948465,
                    -0.6299169984692936,
                    1.0000000000065712],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=3,
                    nanosec=700000000)),
                    trajectory_msgs.msg.JointTrajectoryPoint(
                    positions=[-0.24038610073000477,
                    -0.09724367202365228,
                    -0.7071439834085207,
                    -2.216117700305348,
                    -0.07486531188395262,
                    2.1406618368933086,
                    -0.11926945390282707],
                    velocities=[-3.665584188934365e-17,
                    1.0493486168558249e-16,
                    -1.0783051919435678e-16,
                    2.135993989199773e-17,
                    -1.1416013767355195e-17,
                    8.689728720971001e-17,
                    -1.3795037667096276e-16],
                    accelerations=[0.2657175918806756,
                    -0.7606710776306225,
                    0.7816616510422343,
                    -0.15483785116575433,
                    0.08275449507599832,
                    -0.6299169984427555,
                    0.9999999999644451],
                    effort=[],
                    time_from_start=builtin_interfaces.msg.Duration(
                    sec=3,
                    nanosec=727159453))]),
                    multi_dof_joint_trajectory=trajectory_msgs.msg.MultiDOFJointTrajectory(
                    header=std_msgs.msg.Header(
                    stamp=builtin_interfaces.msg.Time(
                    sec=0,
                    nanosec=0),
                    frame_id=''),
                    joint_names=[],
                    points=[])))

        return execute_msg

    
    async def execute_callback(self,request,response):
 
        exec_msg=self.send_execute()
        self.future_response=await self._execute_client.send_goal_async(exec_msg)
        self.response=await self.future_response.get_result_async()
        self.get_logger().info(f'\nresponse\n{self.response}')

        response=Empty.Response()
        return response 




>>>>>>> ag



def main(args=None):
    rclpy.init(args=args)

<<<<<<< HEAD
    #action_client = Testing()
    newp = Testing()
    # newp.get_ik(0,0,0,0,0,0)
    #future = action_client.send_goal()
    rclpy.spin(newp)
    #rclpy.spin_until_future_complete(action_client,future)
=======
    newp = Testing()
    rclpy.spin(newp)

>>>>>>> ag




