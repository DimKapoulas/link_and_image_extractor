from urllib import robotparser


# Instantiate a robots.txt parser
robot_parser: robotparser.RobotFileParser = robotparser.RobotFileParser()

def prepare(robots_txt_url: str) -> None:
    robot_parser.set_url(robots_txt_url)
    robot_parser.read()

# Check if the target url can be crawled by the given agent
def is_allowed(target_url: str, user_agent: str ='*') -> bool:
    return robot_parser.can_fetch(user_agent, target_url)


if __name__ == '__main__':
    prepare('http://www.apress.com/robots.txt')
    
    print(is_allowed('http://www.apress.com/covers/'))
    print(is_allowed('http://www.apress.com/gp/python'))