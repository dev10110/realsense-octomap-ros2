#include <chrono>
#include <string>


#include <sensor_msgs/msg/point_cloud2.hpp>

#include "rclcpp/rclcpp.hpp"

using std::placeholders::_1;


class ProcessPCL: public rclcpp::Node 
{

  public:
    ProcessPCL() :
      Node("process_pcl")
    {
      
      m_pointCloudSub = this->create_subscription<sensor_msgs::msg::PointCloud2>(
          "/camera/depth/color/points", 1, 
          std::bind(&ProcessPCL::pointCloudCallback, this, _1));
    }


  private:

    rclcpp::Subscription<sensor_msgs::msg::PointCloud2>::SharedPtr m_pointCloudSub;

    void pointCloudCallback( const sensor_msgs::msg::PointCloud2::SharedPtr msg) const
    {

      RCLCPP_INFO(this->get_logger(), "received msg with %d elements", msg->height * msg->width);

    }
};

int main(int argc, char* argv[]){

  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ProcessPCL>());
  rclcpp::shutdown();
  return 0;

}
