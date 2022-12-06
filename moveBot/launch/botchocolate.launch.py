from launch import LaunchDescription, LaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription,DeclareLaunchArgument
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import LaunchConfigurationEquals
from launch.actions import ExecuteProcess


def generate_launch_description():
    '''
    Launches simple_move, vision stuff, and rviz.

    # With the real robot:
    ros2 launch moveBot botchocolate.launch.py real:=true

    # With fake hardware/only rviz on your computer:
    ros2 launch moveBot botchocolate.launch.py real:=false

    '''
     
    use_real_robot = DeclareLaunchArgument(
        "real",
        default_value="true",
        description="Choose whether to use the real robot"
    )
    
    # launches the simple_move launchfile
    simple_move = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [FindPackageShare("moveBot"),"/launch/","simple_move.launch.py"]
        )
    )
        

    rviz_fake = ExecuteProcess(
        cmd=[
            "ros2",
            "launch",
            "franka_moveit_config",
            "moveit.launch.py",
            "robot_ip:=dont-care",
            "use_fake_hardware:=true"
        ],
        condition = LaunchConfigurationEquals("real","false")
    )
    
    rviz_real = ExecuteProcess(
        cmd=[
            "ros2",
            "launch",
            "franka_moveit_config",
            "rviz.launch.py",
            "robot_ip:=panda0.robot",
        ],
        condition = LaunchConfigurationEquals("real","true")
    )

    simple_move = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [FindPackageShare("moveBot"),"/launch/","simple_move.launch.py"]
        )
    )

    vision = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [FindPackageShare("bot_vis"),"/launch/","launch_vision.py"]
        ),
        condition = LaunchConfigurationEquals("real","true")
    )


    ld = LaunchDescription([
        simple_move,
        vision,
        rviz_real,
        rviz_fake,
    ])

    return ld
