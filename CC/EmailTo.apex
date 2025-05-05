public class EmailTo {
    public static void sendEmailMethod(String toAddress, String subject, String body){
        System.debug('Sending Email To: ' + toAddress);
        System.debug('Subject: ' + subject);
        System.debug('Body: ' + body);
        
        Messaging.SingleEmailMessage email = new Messaging.SingleEmailMessage();
        email.setToAddresses(new String[] {toAddress});
        email.setSubject(subject);
        email.setPlainTextBody(body);
        
        Messaging.sendEmail(new Messaging.SingleEmailMessage[] {email});
    }
}



Debug
EmailTo.sendEmailMethod('jagtapaniket7000@gmail.com', 'Test Email', 'Hello from Salesforce!');
