resource "aws_instance" "cerberus" {
  ami = var.ami
  instance_type = var.instance_type
  key_name = aws_key_pair.cerberus-key.id
  user_data = file("/root/terraform-projects/project-cerberus/install-nginx.sh") 
}

resource "aws_key_pair" "cerberus-key" {
  key_name = "cerberus"
  public_key = file("/root/terraform-projects/project-cerberus/.ssh/cerberus.pub")
}

resource "aws_eip" "eip" {
  vpc = true
  instance = aws_instance.cerberus.id
  provisioner "local-exec" {
      command = "echo ${aws_instance.cerberus.public_dns} >> /root/cereberus_public_dns.txt"
  }
  
}