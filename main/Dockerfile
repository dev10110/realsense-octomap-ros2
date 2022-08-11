FROM osrf/ros:galactic-desktop

SHELL ["/bin/bash", "-c"]

# vim and tmux
RUN apt-get update && apt-get install -y vim tmux && rm -rf /var/lib/apt/lists

## install realsense
RUN apt-get update && apt-get install -y \
  ros-galactic-realsense2-camera \
  && rm -rf /var/lib/apt/lists/

# ## install octomap
WORKDIR "/root/"
RUN git clone https://github.com/OctoMap/octomap.git
WORKDIR "/root/octomap/build"
RUN cmake .. && make -j
# set an env variable on where octomap is
ENV octomap_DIR /root/octomap/lib/cmake/octomap/
#ENV OCTOMAP_DIR /root/colcon_ws/src/octomap/lib/cmake/octomap/
 

# add the ros2 sourcing to bashrc
RUN echo "source /opt/ros/galactic/setup.bash" >> /root/.bashrc
RUN echo "source /root/colcon_ws/install/setup.bash" >> /root/.bashrc


WORKDIR "/root/colcon_ws"
