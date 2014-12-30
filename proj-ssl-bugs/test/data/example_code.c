     /*
523      * call our own wrapper
524      */
525     *to_len = 0;
526
527     sc_kmutex_unlock(ssl_keys.lock);
528     keys_locked = sc_false;
529
530     jrsa = jsf_rsa_create_from_openssl_rsa((RSA *)rsa_key);
531
532     if (jrsa) {
533         rc = jsf_crypto_rsa(jsf_rsa_eng,
534                 JCE_OP_RSA_PRIVATE_DECRYPT,
535                 jrsa,
536                 RSA_SSLV23_PADDING, 0,
537                 from,from_len,
538                 to,SC_PKI_PRE_MASTER_SECRET_SIZE+200,
539                 to_len);
540         //SC_COUNTER_INC(sc_ssl_sess_jsf_rsa);
541         sc_kdebug("%s: JSF RSA Eng: %s from_len %d to_len %d\n",
542             __FUNCTION__, jsf_rsa_eng->name, from_len,*to_len);
543     }else{
544         sc_kerror("%s: JRSA create failed. \n", __FUNCTION__);
545     }
546
547     if (!jrsa) {
548         jsf_rsa_release(jrsa);
549     }else {
550         sc_kerror("%s: JRSA return failed. \n", __FUNCTION__);
551     }
552
553     if (rc != JCE_OK) {
554         //SC_COUNTER_INC(sc_ssl_sess_jsf_rsa_failed);
555         sc_kerror("%s: JSF RSA public decrypty failed, "
556             "return value %d\n", __FUNCTION__, rc);
557     }
558
559     if (*to_len <= 0) {
560         if (keys_locked == sc_false) {
561             sc_kmutex_lock(ssl_keys.lock);
562             keys_locked = sc_true;
563         }
564         //SC_COUNTER_INC(sc_ssl_sess_openssl_rsa);
565         *to_len = sc_RSA_private_decrypt(from_len, from, to,
566                                       (RSA *)rsa_key, RSA_SSLV23_PADDING);
