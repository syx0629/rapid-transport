import yaml, os


# This variable should be set as an environment variable
TOPPRA_APP_DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
TOPPRA_APP_MODEL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models"))
# TOPPRA_APP_MODEL_DIR = "~/git/toppra-object-transport/models"
DEFAULT_CONF_FILE = os.path.join(TOPPRA_APP_DATA_DIR, "conf.yaml")


class Database(object):
    """ A simple database to retrieve and insert contact, object, robot, trajectory and algorithm
    profiles.

    """
    def __init__(self):
        self.options = {}
        self.options['contact_profile_dir'] = os.path.join(TOPPRA_APP_DATA_DIR, "contacts.yaml")
        self.options['object_profile_dir'] = os.path.join(TOPPRA_APP_DATA_DIR, "objects.yaml")
        self.options['robot_profile_dir'] = os.path.join(TOPPRA_APP_DATA_DIR, "robots.yaml")
        self.options['trajectory_profile_dir'] = os.path.join(TOPPRA_APP_DATA_DIR, "trajectories.yaml")
        self.options['algorithm_profile_dir'] = os.path.join(TOPPRA_APP_DATA_DIR, "algorithms.yaml")
        self.options['contact_data_dir'] = os.path.join(TOPPRA_APP_DATA_DIR, "contact_data")

        with open(self.options['contact_profile_dir']) as f:
            self.all_contacts = yaml.load(f.read())
        with open(self.options['object_profile_dir']) as f:
            self.all_objects = yaml.load(f.read())
        with open(self.options['trajectory_profile_dir']) as f:
            self.all_trajectories = yaml.load(f.read())
        with open(self.options['robot_profile_dir']) as f:
            self.all_robots = yaml.load(f.read())
        with open(self.options['algorithm_profile_dir']) as f:
            self.all_algorithms = yaml.load(f.read())

    def retrieve_profile(self, obj_id, table):
        """ Retrieve an object profile.

        Parameters
        ----------
        obj_id: str
            Object profile identifier.
        table
            Kind of profile. Can be "contact", "robot", ...etc

        Returns
        -------
        out: dict
            Object profile.
        """
        if table == "contact":
            selected_table = self.all_contacts
        elif table == "object":
            selected_table = self.all_objects
        elif table == "robot":
            selected_table = self.all_robots
        elif table == "trajectory":
            selected_table = self.all_trajectories
        elif table == "algorithm":
            selected_table = self.all_algorithms
        else:
            raise IOError, "Table [{:}] not found!".format(table)

        if obj_id not in selected_table:
            raise ValueError, "Object with id [{:}] not found in table [{:}]".format(obj_id, table)

        return selected_table[obj_id]

    def insert_profile(self, obj_profile, table):
        """ Insert a new profile.

        Parameters
        ----------
        obj_profile: dict
            The object profile to be inserted.
        table: str
            Name of the table.

        """
        if table == 'contact':
            self.all_contacts[obj_profile['id']] = obj_profile
            with open(self.options['contact_profile_dir'], 'w') as yaml_file:
                yaml_file.write(yaml.dump(self.all_contacts))
        elif table == "trajectory":
            self.all_trajectories[obj_profile['id']] = obj_profile
            with open(self.options['trajectory_profile_dir'], 'w') as yaml_file:
                yaml_file.write(yaml.dump(self.all_trajectories))
        else:
            raise NotImplementedError, "Insertion for table {:} is not implemented!".format(table)

    def get_contact_data_dir(self):
        """ Return the path to data storage directory.

        Returns
        -------
        out: str
            Data directory.
        """
        return self.options['contact_data_dir']

    def get_trajectory_data_dir(self):
        """ Return the path to data storage directory.

        Returns
        -------
        out: str
            Data directory.
        """
        return self.options['contact_data_dir']

    def get_data_dir(self):
        """ Return the data directory of toppra_app.
        """
        return TOPPRA_APP_DATA_DIR

    def get_model_dir(self):
        """ Return the model directory of toppra_app.
        """
        return TOPPRA_APP_MODEL_DIR
