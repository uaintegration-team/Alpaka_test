from aws_cdk import core as cdk
from aws_cdk import aws_s3 as s3
import aws_cdk.aws_cloudfront as cloudfront
import aws_cdk.aws_cloudfront_origins as origins
import aws_cdk.aws_iam as iam
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class UaIntAlpackedStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self,
                           id="s3_alpacked",
                           bucket_name="ua-int-alpacked-test",
                           public_read_access=True,
                           website_index_document="index.html",
                           website_error_document="404/index.html"
                           )
        cloudfront.Distribution(self,
            "cfront_alpacked",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(bucket)),
            default_root_object="index.html"
            )

        iam.ManagedPolicy(self,
           "managed-policy-id'", {
           description: 'Acces to S3 bucket',
           statements: [
                         iam.PolicyStatement({
                         effect: iam.Effect.ALLOW,
                         actions: [
                                "s3:PutObject",
                                "s3:GetObject",
                                "s3:ListBucket",
                                "s3:DeleteObject"],
                        resources: [
                               "arn:aws:s3:::*/*",
                               "arn:aws:s3:::ua-int-alpacked-test"
                                 ],
                                 }),
                         ]              
                )
        iam.User(self,
           "My test user",
           user_name="Test_user"
#           managed_policies="S3_acsses_r_w"
)
