*Learn more on the ansible modules

`https://docs.ansible.com/ansible/2.9/modules/list_of_cloud_modules.html`

apt-key addition module `https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_key_module.html`

- name: Delete content & directory
  file:
    state: absent
    path: /home/mydata/web/

- name: Import a key from a url
  ansible.builtin.rpm_key:
    state: present
    key: http://apt.sw.be/RPM-GPG-KEY.dag.txt