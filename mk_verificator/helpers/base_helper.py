def run_dd(ssh_client, count, block_size):
    """Runs dd command with certain count, block size on the certain host"""
    file_name = "test.dat"
    ssh_client.run('rm '.format(file_name))
    ssh_stdout = ssh_client.run(
        'dd if=/dev/zero of={0} oflag=direct bs={1} count={2}'.
        format(file_name, block_size, count))
    if ssh_client.run("echo $?") == '0':
        parsed_result = " ".join(ssh_stdout.split(" ")[-2:])
        return parsed_result
    else:
        raise Exception("The dd command failed:\n{}".format(ssh_stdout))
