import os,sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
services_dir = os.path.abspath(os.path.join(cur_dir, "../services"))

sys.path.append(services_dir)

from data_migrator import service as data_migrator

del sys.path[sys.path.index(services_dir)]


api_objects_config_dict = {
	"v1.1": {
		"data_migrator": {
			"object_instance": data_migrator.Runner()
		}

		
	}
}

if __name__ == "__main__":
	
	pass


