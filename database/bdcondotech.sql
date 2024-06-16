create table gestor (
    idgestor serial not null,
    nomegestor varchar(50),
    cpfgestor varchar(50),
    emailgestor varchar(50),
    senhagestor varchar(50),
    numerotelefonegestor char(11),

    constraint pk_gestor primary key (idgestor)
);

create table local (
    idlocal serial not null,
    nomelocal varchar(50),
    capacidadelocal varchar(10),

    constraint pk_local primary key (idlocal)
);

create table morador (
    idmorador serial not null,
    nomemorador varchar(50),
    cpfmorador varchar(50),
    emailmorador varchar(50),
    senhamorador varchar(50),
    telefonemorador varchar(50),

    constraint pk_morador primary key (idmorador)
);

create table reserva (
    idreserva serial not null,
    diareserva char(2),
    inicioreserva char(5),
    fimreserva char(5),

    idmorador int not null,
    idlocal int not null,

    constraint pk_reserva primary key (idreserva),
    constraint fk_reserva_morador foreign key (idmorador) references morador (idmorador),
    constraint fk_reserva_local foreign key (idlocal) references local (idlocal)

);