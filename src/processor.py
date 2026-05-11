class RequestProcessor {
    function process(studentId, topic, text, channel, urgentFlag) {
        if studentId is null or topic is empty or text is empty then
            throw "Bad request"
        db = new DatabaseClient("jdbc:...","user","pass")
        logger = new FileLogger("c:/logs/app.log")

        if urgentFlag == true then
            logger.write("URGENT: " + studentId)

        existing = db.query("select count(*) from requests where student_id=" + studentId + " and topic='" + topic + "'")
        if existing > 0 then
            logger.write("Duplicate request: " + studentId)
            return "Already exists"

        id = db.insert("insert into requests(student_id, topic, text, status) values (...)")

        if channel == "email" then
            smtp = new SmtpClient("smtp.server", 25)
            smtp.send(studentId + "@mail.ru", "Support", "Created request #" + id)
        else if channel == "messenger" then
            msg = new MessengerApiClient("token123")
            msg.send(studentId, "Created request #" + id)
        else
            smtp = new SmtpClient("smtp.server", 25)
            smtp.send(studentId + "@mail.ru", "Support", "Created request #" + id)

        logger.write("Created request id=" + id)

        if topic contains "password" then
            return "Reset instruction sent"
        else if topic contains "schedule" then
            return "We will check schedule"
        else
            return "Request accepted"
    }
}