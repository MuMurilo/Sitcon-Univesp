PGDMP      1                }            sitcon    17.4    17.4     O           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            P           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            Q           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            R           1262    16388    sitcon    DATABASE     }   CREATE DATABASE sitcon WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE sitcon;
                     postgres    false            �            1259    16389    amv    TABLE     >  CREATE TABLE public.amv (
    idamv integer NOT NULL,
    tipofuncao character varying(5) NOT NULL,
    l1 character varying(8) DEFAULT NULL::character varying,
    l2 character varying(8) DEFAULT NULL::character varying,
    l3 character varying(8) DEFAULT NULL::character varying,
    l4 character varying(8) DEFAULT NULL::character varying,
    l5 character varying(8) DEFAULT NULL::character varying,
    l6 character varying(8) DEFAULT NULL::character varying,
    l7 character varying(8) DEFAULT NULL::character varying,
    l9 character varying(8) DEFAULT NULL::character varying,
    l10 character varying(8) DEFAULT NULL::character varying,
    tower character varying(8) DEFAULT NULL::character varying,
    interface character varying(8) DEFAULT NULL::character varying,
    l14 character varying(8) DEFAULT NULL::character varying,
    l15 character varying(8) DEFAULT NULL::character varying,
    l16 character varying(8) DEFAULT NULL::character varying,
    l17 character varying(8) DEFAULT NULL::character varying,
    l18 character varying(8) DEFAULT NULL::character varying,
    l20 character varying(8) DEFAULT NULL::character varying,
    l21 character varying(8) DEFAULT NULL::character varying,
    l22 character varying(8) DEFAULT NULL::character varying,
    l23 character varying(8) DEFAULT NULL::character varying
);
    DROP TABLE public.amv;
       public         heap r       postgres    false            �            1259    16414    amv_filtrado    VIEW     �  CREATE VIEW public.amv_filtrado AS
 SELECT idamv,
    tipofuncao,
    NULLIF((l1)::text, ''::text) AS l1,
    NULLIF((l2)::text, ''::text) AS l2,
    NULLIF((l3)::text, ''::text) AS l3,
    NULLIF((l4)::text, ''::text) AS l4,
    NULLIF((l5)::text, ''::text) AS l5,
    NULLIF((l6)::text, ''::text) AS l6,
    NULLIF((l7)::text, ''::text) AS l7,
    NULLIF((l9)::text, ''::text) AS l9,
    NULLIF((l10)::text, ''::text) AS l10,
    NULLIF((tower)::text, ''::text) AS tower,
    NULLIF((interface)::text, ''::text) AS interface,
    NULLIF((l14)::text, ''::text) AS l14,
    NULLIF((l15)::text, ''::text) AS l15,
    NULLIF((l16)::text, ''::text) AS l16,
    NULLIF((l17)::text, ''::text) AS l17,
    NULLIF((l18)::text, ''::text) AS l18,
    NULLIF((l20)::text, ''::text) AS l20,
    NULLIF((l21)::text, ''::text) AS l21,
    NULLIF((l22)::text, ''::text) AS l22,
    NULLIF((l23)::text, ''::text) AS l23
   FROM public.amv;
    DROP VIEW public.amv_filtrado;
       public       v       postgres    false    217    217    217    217    217    217    217    217    217    217    217    217    217    217    217    217    217    217    217    217    217    217            �            1259    16418    sinais    TABLE     E  CREATE TABLE public.sinais (
    idsinais integer NOT NULL,
    tipoaspecto character varying(5) NOT NULL,
    l1 character varying(8) DEFAULT NULL::character varying,
    l2 character varying(8) DEFAULT NULL::character varying,
    l3 character varying(8) DEFAULT NULL::character varying,
    l4 character varying(8) DEFAULT NULL::character varying,
    l5 character varying(8) DEFAULT NULL::character varying,
    l6 character varying(8) DEFAULT NULL::character varying,
    l7 character varying(8) DEFAULT NULL::character varying,
    l8 character varying(8) DEFAULT NULL::character varying,
    l10 character varying(8) DEFAULT NULL::character varying,
    tower character varying(8) DEFAULT NULL::character varying,
    interface character varying(8) DEFAULT NULL::character varying,
    l14 character varying(8) DEFAULT NULL::character varying,
    l15 character varying(8) DEFAULT NULL::character varying,
    l16 character varying(8) DEFAULT NULL::character varying,
    l18 character varying(8) DEFAULT NULL::character varying,
    l19 character varying(8) DEFAULT NULL::character varying,
    l20 character varying(8) DEFAULT NULL::character varying,
    l21 character varying(8) DEFAULT NULL::character varying,
    l22 character varying(8) DEFAULT NULL::character varying,
    l23 character varying(8) DEFAULT NULL::character varying
);
    DROP TABLE public.sinais;
       public         heap r       postgres    false            K          0    16389    amv 
   TABLE DATA           �   COPY public.amv (idamv, tipofuncao, l1, l2, l3, l4, l5, l6, l7, l9, l10, tower, interface, l14, l15, l16, l17, l18, l20, l21, l22, l23) FROM stdin;
    public               postgres    false    217   �       L          0    16418    sinais 
   TABLE DATA           �   COPY public.sinais (idsinais, tipoaspecto, l1, l2, l3, l4, l5, l6, l7, l8, l10, tower, interface, l14, l15, l16, l18, l19, l20, l21, l22, l23) FROM stdin;
    public               postgres    false    219          �           2606    16413    amv amv_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.amv
    ADD CONSTRAINT amv_pkey PRIMARY KEY (idamv, tipofuncao);
 6   ALTER TABLE ONLY public.amv DROP CONSTRAINT amv_pkey;
       public                 postgres    false    217    217            �           2606    16442    sinais sinais_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.sinais
    ADD CONSTRAINT sinais_pkey PRIMARY KEY (idsinais, tipoaspecto);
 <   ALTER TABLE ONLY public.sinais DROP CONSTRAINT sinais_pkey;
       public                 postgres    false    219    219            K   C  x�}��n� е�/�`�Y�N�QeEj*�G����x�����`<����粜۵Y����Iۏm?�N2�e�R�`�nQ��X�G!�
@��C!$��@�"�A����Oxm�7�5��қV7EQ��;�X�'�YЮQ�z�vAV� D������:�����}�:�H�/�]�s7ۗ��K�����i�
��1�� �@T�E�������MP����O/�u ��[��̥��ye����R�n�8�����0���¼�]��j�b(+����Ja�,3_y��3���i�,�(6���댬VsV���6e=����Fî�[�`���`���E�G��T����S�����;p�Ѳ\���彑�\�ȸ&�{���Mۅr��_���`S��a���N���w�����<F�%3�^
N��._�GǗ��z��>�v��2.bc�s.!�`MĥM�ձ�2O)�Ȧ�:!mi����32�}�W�l�3p`C��0�0�~�D���J��fY��Q�0vF�i�q���1����㣰��3�!L:� �3��W1⴮��<S������?1@R�      L   m  x�}����,��.�HQ".cO'�,rf1���� Up����?/WP�����t���hJ���1/.�i�<h~��:�|8?S���{pV��-Ցu�֝H㪂U*t
i��h�/J��|(�9�K}�k,��nA��c�`��֝5-��Ũ�@�N!���N:8�-�V)�\��,y6L�6��<�^�7Pǹ6�<����zv�m
�S��t�&�3t5{��Ah�꼁�!��9mF� ��fDK��H+ =��A�#�5=h�2ăpC�&#��g�]F4$��������c��{��pC���3�/�2�=�գ��)~�W��J�D\۞��u�Sϻk��2'�]3ʩu�����<|~/�;M��zꀽ��D��KΛ� �k����h`!+�=����W�r��!Ch3Z�B�w����w��2�q>>t�����
�{�����o�L���&����
�yX2�=\��·�ͼ��z��VQ��y��zΙ?O�f���o��͎8L�WaX�<��3�0�2�,��S��� �79��&# dPn26�� �:�TUvD�d�����g�tG��]����;"�+÷`̐1dP�1�C� �>�k=*���k�;�]��2�����7!�D���b�<'��z�3��u��ye�-kS�'��._\��-Z�M�K���!�O��KI�gv��p�gN�ݟ��+�l�c��k j^�߅Ȧ�	5�l2��4��g�]F���ˠ��3�b�0m2h�Q��x�6���{E�~4v}��S ��:T��O}���f�kO&D�*��g�A�p���e�CF��J�d�e��A�|��7`�{
	 ���p�W~��{8T��|g���x<�?�93     