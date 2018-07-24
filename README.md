# Cobbler + cloud-init

These files are the only files that required modification from a typical Cobbler installation. There are two different methods to provide cloud-init with Cobbler. One is using the `add-kernel-opts` directive in preseed, and the other is to use a Python script that is triggered automatically during machine installation.

The sample.seed file adds the cloud-init datasource as a string using `add-kernel-opts` directive. This allows for the Cheetah templated hostname and UID variables to act as hostname and instance ID metadata, respectively. Cobbler can then host the meta-data (an emply file in this case), and the user-data files in the directory /var/www/cobbler/localmirror/mds/.

The sample-python.seed file still adds the cloud-init datasource using `add-kernel-opts`, but here the installation triggers a Python script that automatically creates instance metadata in the /var/www/cobbler/localmirror/mds/<hostname> directory.
  
The preseed_late_default script was modified to remove the late_apt_repo_config so that the repo could be created by the preseed_late_command.
