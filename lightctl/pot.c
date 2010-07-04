void sensor_display(){
    adc_start(ADC_MUX_PIN_F0, ADC_REF_POWER);
    uint8_t full = 255;
    uint8_t off = 0;
    while(1){
        val=adc_read();
        if (val < 100){
            OCR0B = off;
            OCR1A = off;
            OCR2A = off;
            OCR2B = off;
        }
        else{
        if (val < 200){
            OCR0B = off;
            OCR1A = off;
            OCR2A = off;
            OCR2B = full;
        }
        else{
        if (val < 300){
            OCR0B = off;
            OCR1A = off;
            OCR2A = full;
            OCR2B = off;
        }
        else{
        if (val < 400){
            OCR0B = off;
            OCR1A = off;
            OCR2A = full;
            OCR2B = full;
        }      
        else{
        if (val < 500){
            OCR0B = full;
            OCR1A = off;
            OCR2A = off;
            OCR2B = off;
        }
        else{
        if (val < 600){
            OCR0B = full;
            OCR1A = off;
            OCR2A = off;
            OCR2B = full;
        }  
        else{
        if (val < 700){
            OCR0B = full;
            OCR1A = off;
            OCR2A = full;
            OCR2B = off;
        } 
        else{
        if (val < 800){
            OCR0B = full;
            OCR1A = off;
            OCR2A = full;
            OCR2B = full;
        } 
        else{
        if (val < 900){
            OCR0B = off;
            OCR1A = full;
            OCR2A = off;
            OCR2B = off;
        }
        else{
        if (val < 1000){
            OCR0B = off;
            OCR1A = full;
            OCR2A = off;
            OCR2B = full;
        }
        }}}}}}}}}}


}}
