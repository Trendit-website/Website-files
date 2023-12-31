import React from "react";
import { ArrowBackIcon } from "@chakra-ui/icons";
import { IconButton } from "@chakra-ui/react";

import { Box, Flex, Text, Heading, Button, Container } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import { ArrowForwardIcon } from "@chakra-ui/icons";
import {colors} from "../../components/colors"

const cardContent = [
  {
    icon: "bi:phone-vibrate-fill",
    header: "Social tasks",
    content:
      "Our platform features a variety of income-generating strategies for users by having them carry out simple social media activities.",
    to: "/earn/adverts-tasks",
    text: "Get started",
  },
  {
    icon: "healthicons:money-bag",
    header: "Resell",
    content:
      "We connect you to real people that will help you achieve your business goals in a way that is both effective and cost-efficient.",
    to: "/market-place",
    text: "Go to market place",
  },
];

const Card = ({ icon, header, content, to, text }) => {
  const navigate = useNavigate();
  return (
    <Box
      bg={colors.secondarybg}
      p={4}
      shadow="md"
      borderRadius="md"
      width={{ base: "85%", md: "350px" }}
      height="300px"
      mx="20px"
      my={4}
      mt={20}
    >
      <Box alignItems="center" p={1}>
        <Box
          bg="#222222"
          w={10}
          h={10}
          borderRadius="md"
          marginRight={4}
          mt={2}
          mb={6}
          display="flex"
          justifyContent="center"
          alignItems="center"
        >
          <iconify-icon
            icon={icon}
            style={{ color: colors.primaryText }}
            width="30"
          ></iconify-icon>
        </Box>
        <Box>
          <Heading
            as="h2"
            size="md"
            display="flex"
            mt={0}
            mb={1}
            color=" #CB29BE"
            fontFamily="Clash Grotesk"
            fontWeight="600"
          >
            {header}
          </Heading>
          <Text fontSize="15px" py={0} letterSpacing="0.369px" color={colors.primaryText}>
            {content}
          </Text>
        </Box>
      </Box>
      <Button
        width="full"
        rounded="full"
        bg={colors.secondary}
        fontWeight="400"
        color="white"
        mt={8}
        mb={0}
        onClick={() => navigate(to)}
        _hover={{
          bg:colors.primarybg,
          color: "white",
          opacity: "0.9",
        }}
      >
        {text}
        <ArrowForwardIcon ml={3} />
      </Button>
    </Box>
  );
};

const Goback = () => {
  const navigate = useNavigate();
  const handleGoBack = () => {
    navigate(-1); // Go back to the previous route
  };
  return (
    <Box bg="black" pr="100%" py={10}>
      <IconButton
        onClick={handleGoBack}
        left={{ base: "8px", md: '25%', lg: "25%", '2xl': '32%' }} 
        py={6}
        pr={100}
        pos="fixed"
        top="88px"
        zIndex="1000"
       mb={10}
        color="white"
        bg="black"
        _hover={{ bg: "inherit" }}
        fontSize="30px"
        cursor="pointer"
        icon={<ArrowBackIcon />}
      />
    </Box>
  );
};

export { Goback };

const CardsSection = () => {
  return (
    <Container
      ml={{ base: 0, md: "25%" }}
      p={{ base: "4", md: "10" }}
      maxW={{ base: "100%", md: "75%" }}
      bg="black"
      height={{ base: "full", md: "100vh" }}
     
     
      fontFamily="clash grotesk"
    >
      <Box my={5}  pt={20}>
        <Flex
          direction={{ base: "column", md: "row" }}
          align={{ base: "center", md: "center" }}
          justify={{ base: "center", md: "space-between" }}
          justifyContent="center"
          wrap="wrap"
          fontFamily="Clash Grotesk"
        >
          {cardContent.map((card, index) => (
            <Card
              key={index}
              icon={card.icon}
              header={card.header}
              content={card.content}
              to={card.to}
              text={card.text}
            />
          ))}
        </Flex>
      </Box>
      <Goback />
    </Container>
  );
};

export default CardsSection;
