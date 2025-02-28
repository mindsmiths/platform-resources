package com.mindsmiths.{{cookiecutter.service_name_camel_case.lower()}};

import com.mindsmiths.sdk.core.api.Message;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;


@Data
@NoArgsConstructor
@AllArgsConstructor
public class DoSomething extends Message {
    private String someData;  // TODO: change this
}
