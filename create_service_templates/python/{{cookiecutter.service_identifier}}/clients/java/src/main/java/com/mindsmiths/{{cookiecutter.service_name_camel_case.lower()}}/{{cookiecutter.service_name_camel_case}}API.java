package com.mindsmiths.{{cookiecutter.service_name_camel_case.lower()}};


public class {{cookiecutter.service_name_camel_case}}API {
    private static final String serviceId = "{{cookiecutter.service_identifier}}";

    // TODO: change this
    public static DoSomething doSomething(String someData) {
        DoSomething message = new DoSomething(someData);
        message.send(serviceId);
        return message;
    }
}
