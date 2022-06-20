package com.mindsmiths.{{cookiecutter.service_name_camel_case.lower()}};

import java.io.Serializable;

import com.mindsmiths.sdk.core.api.BaseMessage;
import com.mindsmiths.sdk.core.api.CallbackResult;
import com.mindsmiths.sdk.messaging.Messaging;


public class {{cookiecutter.service_name_camel_case}}API {
    private static final String topic = Messaging.getInputTopicName("{{cookiecutter.service_identifier}}");

    // TODO: change this
    public static void doSomething(String someData) {
        Serializable payload = new DoSomethingPayload(someData);
        BaseMessage message = new BaseMessage("DO_SOMETHING", payload);
        message.send(topic);
        new CallbackResult(message.getConfiguration().getMessageId(), Result.class).save();
    }
}
