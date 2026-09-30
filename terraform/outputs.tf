output "ec2_public_ip" {
  description = "Public IP Address of the EC2 instance"
  value       = aws_instance.main_instance.public_ip
}

output "ecr_repository_url" {
  description = "ECR Repository URL"
  value       = aws_ecr_repository.main_ecr.repository_url
}
