AWS()                                                                    AWS()



NNAAMMEE
       aws -

DDEESSCCRRIIPPTTIIOONN
       The  AWS  Command  Line  Interface is a unified tool to manage your AWS
       services.

SSYYNNOOPPSSIISS
          aws [options] <command> <subcommand> [parameters]

       Use _a_w_s _c_o_m_m_a_n_d _h_e_l_p for information on a  specific  command.  Use  _a_w_s
       _h_e_l_p  _t_o_p_i_c_s  to view a list of available help topics. The synopsis for
       each command shows its parameters and their usage. Optional  parameters
       are shown in square brackets.

OOPPTTIIOONNSS
       ----ddeebbuugg (boolean)

       Turn on debug logging.

       ----eennddppooiinntt--uurrll (string)

       Override command's default URL with the given URL.

       ----nnoo--vveerriiffyy--ssssll (boolean)

       By  default, the AWS CLI uses SSL when communicating with AWS services.
       For each SSL connection, the AWS CLI will verify SSL certificates. This
       option overrides the default behavior of verifying SSL certificates.

       ----nnoo--ppaaggiinnaattee (boolean)

       Disable automatic pagination.

       ----oouuttppuutt (string)

       The formatting style for command output.

       +o json

       +o text

       +o table

       +o yaml

       +o yaml-stream

       ----qquueerryy (string)

       A JMESPath query to use in filtering the response data.

       ----pprrooffiillee (string)

       Use a specific profile from your credential file.

       ----rreeggiioonn (string)

       The region to use. Overrides config/env settings.

       ----vveerrssiioonn (string)

       Display the version of this tool.

       ----ccoolloorr (string)

       Turn on/off color output.

       +o on

       +o off

       +o auto

       ----nnoo--ssiiggnn--rreeqquueesstt (boolean)

       Do  not  sign requests. Credentials will not be loaded if this argument
       is provided.

       ----ccaa--bbuunnddllee (string)

       The CA certificate bundle to use when verifying SSL certificates. Over-
       rides config/env settings.

       ----ccllii--rreeaadd--ttiimmeeoouutt (int)

       The  maximum socket read time in seconds. If the value is set to 0, the
       socket read will be blocking and not timeout. The default value  is  60
       seconds.

       ----ccllii--ccoonnnneecctt--ttiimmeeoouutt (int)

       The  maximum  socket connect time in seconds. If the value is set to 0,
       the socket connect will be blocking and not timeout. The default  value
       is 60 seconds.

       ----ccllii--bbiinnaarryy--ffoorrmmaatt (string)

       The formatting style to be used for binary blobs. The default format is
       base64. The base64 format expects binary blobs  to  be  provided  as  a
       base64  encoded string. The raw-in-base64-out format preserves compati-
       bility with AWS CLI V1 behavior and binary values must be passed liter-
       ally.  When  providing  contents  from a file that map to a binary blob
       ffiilleebb:://// will always be treated as binary and  use  the  file  contents
       directly  regardless  of  the  ccllii--bbiinnaarryy--ffoorrmmaatt  setting.  When  using
       ffiillee:://// the file contents will need to properly formatted for the  con-
       figured ccllii--bbiinnaarryy--ffoorrmmaatt.

       +o base64

       +o raw-in-base64-out

       ----nnoo--ccllii--ppaaggeerr (boolean)

       Disable cli pager for output.

       ----ccllii--aauuttoo--pprroommpptt (boolean)

       Automatically prompt for CLI input parameters.

       ----nnoo--ccllii--aauuttoo--pprroommpptt (boolean)

       Disable automatically prompt for CLI input parameters.

AAVVAAIILLAABBLLEE SSEERRVVIICCEESS
       +o accessanalyzer

       +o account

       +o acm

       +o acm-pca

       +o alexaforbusiness

       +o amp

       +o amplify

       +o amplifybackend

       +o amplifyuibuilder

       +o apigateway

       +o apigatewaymanagementapi

       +o apigatewayv2

       +o appconfig

       +o appconfigdata

       +o appflow

       +o appintegrations

       +o application-autoscaling

       +o application-insights

       +o applicationcostprofiler

       +o appmesh

       +o apprunner

       +o appstream

       +o appsync

       +o athena

       +o auditmanager

       +o autoscaling

       +o autoscaling-plans

       +o backup

       +o backup-gateway

       +o batch

       +o billingconductor

       +o braket

       +o budgets

       +o ce

       +o chime

       +o chime-sdk-identity

       +o chime-sdk-media-pipelines

       +o chime-sdk-meetings

       +o chime-sdk-messaging

       +o cli-dev

       +o cloud9

       +o cloudcontrol

       +o clouddirectory

       +o cloudformation

       +o cloudfront

       +o cloudhsm

       +o cloudhsmv2

       +o cloudsearch

       +o cloudsearchdomain

       +o cloudtrail

       +o cloudwatch

       +o codeartifact

       +o codebuild

       +o codecommit

       +o codeguru-reviewer

       +o codeguruprofiler

       +o codepipeline

       +o codestar

       +o codestar-connections

       +o codestar-notifications

       +o cognito-identity

       +o cognito-idp

       +o cognito-sync

       +o comprehend

       +o comprehendmedical

       +o compute-optimizer

       +o configservice

       +o configure

       +o connect

       +o connect-contact-lens

       +o connectparticipant

       +o cur

       +o customer-profiles

       +o databrew

       +o dataexchange

       +o datapipeline

       +o datasync

       +o dax

       +o ddb

       +o deploy

       +o detective

       +o devicefarm

       +o devops-guru

       +o directconnect

       +o discovery

       +o dlm

       +o dms

       +o docdb

       +o drs

       +o ds

       +o dynamodb

       +o dynamodbstreams

       +o ebs

       +o ec2

       +o ec2-instance-connect

       +o ecr

       +o ecr-public

       +o ecs

       +o efs

       +o eks

       +o elastic-inference

       +o elasticache

       +o elasticbeanstalk

       +o elastictranscoder

       +o elb

       +o elbv2

       +o emr

       +o emr-containers

       +o es

       +o events

       +o evidently

       +o finspace

       +o finspace-data

       +o firehose

       +o fis

       +o fms

       +o forecast

       +o forecastquery

       +o frauddetector

       +o fsx

       +o gamelift

       +o gamesparks

       +o glacier

       +o globalaccelerator

       +o glue

       +o grafana

       +o greengrass

       +o greengrassv2

       +o groundstation

       +o guardduty

       +o health

       +o healthlake

       +o help

       +o history

       +o honeycode

       +o iam

       +o identitystore

       +o imagebuilder

       +o importexport

       +o inspector

       +o inspector2

       +o iot

       +o iot-data

       +o iot-jobs-data

       +o iot1click-devices

       +o iot1click-projects

       +o iotanalytics

       +o iotdeviceadvisor

       +o iotevents

       +o iotevents-data

       +o iotfleethub

       +o iotsecuretunneling

       +o iotsitewise

       +o iotthingsgraph

       +o iottwinmaker

       +o iotwireless

       +o ivs

       +o ivschat

       +o kafka

       +o kafkaconnect

       +o kendra

       +o keyspaces

       +o kinesis

       +o kinesis-video-archived-media

       +o kinesis-video-media

       +o kinesis-video-signaling

       +o kinesisanalytics

       +o kinesisanalyticsv2

       +o kinesisvideo

       +o kms

       +o lakeformation

       +o lambda

       +o lex-models

       +o lex-runtime

       +o lexv2-models

       +o lexv2-runtime

       +o license-manager

       +o lightsail

       +o location

       +o logs

       +o lookoutequipment

       +o lookoutmetrics

       +o lookoutvision

       +o machinelearning

       +o macie

       +o macie2

       +o managedblockchain

       +o marketplace-catalog

       +o marketplace-entitlement

       +o marketplacecommerceanalytics

       +o mediaconnect

       +o mediaconvert

       +o medialive

       +o mediapackage

       +o mediapackage-vod

       +o mediastore

       +o mediastore-data

       +o mediatailor

       +o memorydb

       +o meteringmarketplace

       +o mgh

       +o mgn

       +o migration-hub-refactor-spaces

       +o migrationhub-config

       +o migrationhubstrategy

       +o mobile

       +o mq

       +o mturk

       +o mwaa

       +o neptune

       +o network-firewall

       +o networkmanager

       +o nimble

       +o opensearch

       +o opsworks

       +o opsworks-cm

       +o organizations

       +o outposts

       +o panorama

       +o personalize

       +o personalize-events

       +o personalize-runtime

       +o pi

       +o pinpoint

       +o pinpoint-email

       +o pinpoint-sms-voice

       +o pinpoint-sms-voice-v2

       +o polly

       +o pricing

       +o proton

       +o qldb

       +o qldb-session

       +o quicksight

       +o ram

       +o rbin

       +o rds

       +o rds-data

       +o redshift

       +o redshift-data

       +o rekognition

       +o resiliencehub

       +o resource-groups

       +o resourcegroupstaggingapi

       +o robomaker

       +o route53

       +o route53-recovery-cluster

       +o route53-recovery-control-config

       +o route53-recovery-readiness

       +o route53domains

       +o route53resolver

       +o rum

       +o s3

       +o s3api

       +o s3control

       +o s3outposts

       +o sagemaker

       +o sagemaker-a2i-runtime

       +o sagemaker-edge

       +o sagemaker-featurestore-runtime

       +o sagemaker-runtime

       +o savingsplans

       +o schemas

       +o sdb

       +o secretsmanager

       +o securityhub

       +o serverlessrepo

       +o service-quotas

       +o servicecatalog

       +o servicecatalog-appregistry

       +o servicediscovery

       +o ses

       +o sesv2

       +o shield

       +o signer

       +o sms

       +o snow-device-management

       +o snowball

       +o sns

       +o sqs

       +o ssm

       +o ssm-contacts

       +o ssm-incidents

       +o sso

       +o sso-admin

       +o sso-oidc

       +o stepfunctions

       +o storagegateway

       +o sts

       +o support

       +o swf

       +o synthetics

       +o textract

       +o timestream-query

       +o timestream-write

       +o transcribe

       +o transfer

       +o translate

       +o voice-id

       +o waf

       +o waf-regional

       +o wafv2

       +o wellarchitected

       +o wisdom

       +o workdocs

       +o worklink

       +o workmail

       +o workmailmessageflow

       +o workspaces

       +o workspaces-web

       +o xray

SSEEEE AALLSSOO
       +o aws help topics



                                                                         AWS()
