def neuronCaulculation(now,past):
    for neurons in list(now.keys()):
        value = now.get(neurons)
        connect = value.get("connect")
        weight = value.get("weight")
        bias = value.get("bias")
        input_have = 0

        for past_nerrons in connect:
            past_value = past.get(past_nerrons)
            past_input = past_value.get("value")
            input_have += past_input
        value["input"] = input_have

        new_have = input_have * weight + bias
        value["value"] = new_have
        now[neurons] = value
