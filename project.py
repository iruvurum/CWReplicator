Enecccbdncnbigjerkvfgknnhiuhhuvcdbetcrllrubr
import os
import re
def print_error_logs(path):
    
    file=open(path,"r")
    count=0
    sn=1

    regex1=re.compile(r"(.*InvalidSequenceTokenException.*\d+)")
    regex2=re.compile(r"(.*InvalidSequenceTokenException.*The next expected sequenceToken is: null.*)")
    regex3=re.compile(r"(.*CreateLogStream / CreateLogGroup.*InvalidSignatureException.*5 min.*)")
#    regex4=re.compile(r"(.*CreateLogStream / CreateLogGroup.*ResourceNotFoundException.*)")
    regex5=re.compile(r"(.*unable to get response from.*/metadata.*)")
    regex6=re.compile(r"(.*http.*/metadata.*request canceled while waiting for connection)")

    print("Common Error Logs Detected are:-\n")
    for line in file:
        count += 1
        if "InvalidParameterException" in line:
            print(str(sn)+". "+"InvalidParameterException detected in line "+str(count))
            print(line)
            sn+=1

        if regex1.search(line):
            print(str(sn)+". "+"InvalidSequenceTokenException is detected in line "+str(count))
            print(line)
            print("Note that invalid sequence token error once on the agent starts/restarts is fine and expected behaviour as per design of the agent ",end="")
            print("If the error is occuring more than once, there are possibly multiple agents pushing to the same log group because either: ")
            print("a. Customer has multiple agents running on the instance. You can check if this indeed the case with \"ps -aux | grep amazon\" on the instance, or,")
            print("b. Baked AMI copied over stale configuration files (refer to Windows baked AMI under Miscellaneous section below)")
            print("")
            sn+=1

        if "ExpiredToken" in line:
            print(str(sn)+". "+"ExpiredToken Message  detected in line "+str(count))
            print(line)
            sn+=1

        if regex2.search(line):
            print(str(sn)+". "+"InvalidSequenceTokenException  detected in line "+str(count))
            print(line)
            sn+=1
       
        if regex3.search(line):
            print(str(sn)+"."+"Detected error in CreateLogStream / CreateLogGroup in line "+str(count))
            print(line)
            print("The clock on the EC2 Instance where the CW Agent is installed is out of sync with AWS and is more than 5 minutes into the future. AWS doesn\"t allow API calls to it\"s services with a sync gap over 5 minutes.")
            print("To fix this you can install NTP (Network Time Protocol) on the instance to re-synchronize computer system clock.")
            print('')
            sn+=1

##        if regex4.search(line):
##            print(str(sn)+"."+"Detected error in CreateLogStream / CreateLogGroup in line "+str(count))
##            print(line)
##            sn+=1

        if "unable to create the resource access policy" in line.lower():
            print(str(sn)+". "+"Unable to create resource access policy detected in line "+str(count))
            print(line)
            print("This is the maximum number of resource policies you can have in your account for a single region and this is a hard limit so we cannot increase this.")
            print("You can use this command to check all the available resource policies:")
            print("aws logs describe-resource-policies --region some_name")
            print("https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeResourcePolicies.html")
            print("For deleting you can use the command delete-resource-policy")
            print("https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteResourcePolicy.html")
            print('')
            sn+=1

        if "timestamp could not be parsed from message" in line.lower():
            print(str(sn)+". "+"Detected timestamp error in line "+str(count))
            print(line)
            print("Compare the configured date time format with the time stamp of the log events and use correct format")
            print('')
            sn+=1

        if (("unable to get ecs metadata" in line.lower()) or (regex5.search(line)) or (regex6.search(line))):
            print(str(sn)+". "+"Detected error while connecting to ecs metadata endpoint in line "+str(count))
            print(line)
            sn+=1

        if "ec2metadata is not available" in line.lower():
            print(str(sn)+". "+"Detected error in retrieving instance metadata in line "+str(count))
            print(line)
            sn+=1

        if "timestamp is more than 2 hours in future" in line.lower() or "timestamp is more than 14 days in past" in line.lower():
            print(str(sn)+". "+"Detected timestamp error in line "+str(count))
            print(line)
            print("The agent will skip the events if the time stamp in the log event is more than 2 hours in the future or more than 14 days in the past.")
            print("Check the agent configuration and add time_zome parameter")
            print("This parameter represents the time zone of your log event timestamp. The two supported values are UTC and LOCAL. By default if the agent configuration file doesn\"t have this parameter it will use it as LOCAL")
            print("If the customers application is generating the logs in UTC however the EC2 system is in PDT time zone, then you will see such behavior.")
            print('')
            sn+=1

        if "NoCredentialsError" in line:
            print(str(sn)+". "+"NoCredentials detected in line "+str(count))
            print(line)
            sn+=1

        if "DataAlreadyAcceptedException" in line:
            print(str(sn)+". "+"DataAlreadyAcceptedException detected in line "+str(count))
            print(line)
            sn+=1

        if "LimitExceededException" in line:
            print(str(sn)+". "+"LimitExceededException detected in line "+str(count))
            print(line)
            sn+=1

        if "MalformedQueryException" in line:
            print(str(sn)+". "+"MalformedQueryException detected in line "+str(count))
            print(line)
            sn+=1

        if "OperationAbortedException" in line:
            print(str(sn)+". "+"OperationAbortedException detected in line "+str(count))
            print(line)
            sn+=1

        if "ResourceAlreadyExistsException" in line:
            print(str(sn)+". "+"ResourceAlreadyExistsException detected in line "+str(count))
            print(line)
            sn+=1

        if "ResourceNotFoundException" in line:
            print(str(sn)+". "+"ResourceNotFoundException detected in line "+str(count))
            print(line)
            sn+=1

        if "ServiceUnavailableException" in line:
            print(str(sn)+". "+"ServiceUnavailableException detected in line "+str(count))
            print(line)
            sn+=1

        if "UnrecognizedClientException" in line:
            print(str(sn)+". "+"UnrecognizedClientException detected in line "+str(count))
            print(line)
            sn+=1

        if "NoCredentialProviders" in line:
            print(str(sn)+". "+"NoCredentialProviders message detected in line "+str(count))
            print(line)
            sn+=1

        if "SerializationException" in line:
            print(str(sn)+". "+"SerializationException detected in line "+str(count))
            print(line)
            sn+=1


if __name__ == "__main__":
    path=input()
    if(path):
        print_error_logs(path)

