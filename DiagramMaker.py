from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import Route53, CloudFront, ELB, DirectConnect, APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.compute import ElasticBeanstalk, EC2
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.security import Cognito, IAM, WAF, KMS
from diagrams.aws.analytics import EMR, Athena, Glue, Quicksight
from diagrams.aws.management import Cloudwatch, SystemsManager, Cloudtrail

graph_attr = {
    "fontsize": "45",
    "bgcolor": "white",
    "nodesep": "1.0",
    "ranksep": "1.0",
    "size": "20,20"
}

with Diagram("AWS Cloud Migration Architecture", show=False, direction="TB", outformat="png", graph_attr=graph_attr):
    dns = Route53("Route 53")
    cdn = CloudFront("CloudFront")
    waf = WAF("WAF")

    with Cluster("VPC"):
        # Frontend
        with Cluster("Frontend"):
            alb = ELB("Application Load Balancer")
            with Cluster("Auto Scaling Group"):
                ec2 = EC2("EC2 Instances\n(Dynamic Website)")

        # Backend
        with Cluster("Backend"):
            api = APIGateway("API Gateway")
            beanstalk = ElasticBeanstalk("Elastic Beanstalk")
            cognito = Cognito("Cognito")

        # Database
        with Cluster("Database"):
            rds = RDS("RDS MySQL")
            cache = ElastiCache("ElastiCache")

        # Data Analytics
        with Cluster("Data Analytics"):
            data_lake = S3("S3 (Data Lake)")
            emr = EMR("EMR")
            glue = Glue("Glue")
            athena = Athena("Athena")
            quicksight = Quicksight("QuickSight")

        # Security and Management
        with Cluster("Security & Management"):
            iam = IAM("IAM")
            kms = KMS("KMS")
            cloudwatch = Cloudwatch("CloudWatch")
            cloudtrail = Cloudtrail("CloudTrail")
            ssm = SystemsManager("Systems Manager")

    # On-premises connection
    dc = DirectConnect("Direct Connect")

    # Connections
    dns >> Edge(color="darkgreen") >> cdn >> Edge(color="darkgreen") >> waf >> Edge(color="darkgreen") >> alb
    alb >> Edge(color="darkgreen") >> ec2
    ec2 >> Edge(color="darkblue") >> api >> Edge(color="darkblue") >> beanstalk
    cognito >> Edge(color="red", style="dashed") >> api
    beanstalk >> Edge(color="darkorange") >> rds
    beanstalk >> Edge(color="darkorange", style="dashed") >> cache
    
    data_lake >> Edge(color="purple") >> [emr, glue, athena]
    [emr, athena, glue] >> Edge(color="purple") >> quicksight
    
    dc >> Edge(color="brown", label="VPN") >> alb
    
    # Security and management connections
    Edge(color="red", style="dashed") << [ec2, beanstalk, emr, glue, athena, quicksight, rds, api] >> iam
    Edge(color="darkred", style="dotted") << [data_lake, rds] >> kms
    Edge(color="darkgreen", style="dotted") << [ec2, beanstalk, emr, rds, cache] >> cloudwatch
    Edge(color="darkgreen", style="dotted") << [ec2, beanstalk] >> ssm
    cloudtrail >> Edge(color="darkgreen", style="dotted") >> data_lake