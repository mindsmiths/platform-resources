package com.mindsmiths.{{cookiecutter.service_name_camel_case.lower()}};

import com.mindsmiths.sdk.core.api.Reply;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;


@Data
@NoArgsConstructor
@AllArgsConstructor
public class Result extends Reply {
    private boolean success;  // TODO: change this
}
