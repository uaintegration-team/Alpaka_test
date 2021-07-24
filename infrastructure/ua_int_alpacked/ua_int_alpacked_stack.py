from aws_cdk import core as cdk
from aws_cdk import aws_s3 as s3
import aws_cdk.aws_cloudfront as cloudfront
import aws_cdk.aws_cloudfront_origins as origins
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
