import pytest, transport
import openravepy as orpy


@pytest.fixture(scope="session")
def setup():
    env = orpy.Environment()
    yield env
    env.Destroy()
    orpy.RaveDestroy()


@pytest.fixture(scope="module")
def envlab1(setup):
    env = setup
    env.Reset()
    env.Load('data/lab1.env.xml')
    robot = env.GetRobots()[0]
    robot.SetActiveDOFs(range(6))
    yield robot


@pytest.fixture(scope="module")
def envcage(setup):
    env = setup
    env.Reset()
    db = transport.database.Database()
    env.Load(transport.utils.expand_and_join(
        db.get_model_dir(), "caged_denso_ft_sensor_suction.env.xml"))
    robot = env.GetRobots()[0]
    robot.SetActiveDOFs(range(6))
    yield env

