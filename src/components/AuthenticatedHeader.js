import { useDispatch, useSelector } from "react-redux";

import {
  Box,
  Container,
  Flex,
  IconButton,
  Image,
  Input,
  useColorModeValue,
  Text,
  VStack,
  HStack,
  Menu,
  MenuButton,
  MenuItem,
  MenuList,
  Avatar,
  CloseButton,
  Drawer,
  DrawerContent,
  useDisclosure,
} from "@chakra-ui/react";
import { FiMenu, FiBell, FiChevronDown, FiSearch } from "react-icons/fi";
import {
  NavLink,
  useLocation,
  useMatch,
  Outlet,
  useNavigate,
} from "react-router-dom";
import Logo from "../../src/assets/images/logo.png";
import { logout } from "../services/slices/authSlice";

const LinkItems = [
  { name: "Home", icon: "solar:cart-4-bold", path: "/homepage" },
  { name: "Earn", icon: "healthicons:money-bag", path: "/earn" },
  { name: "Advertise", icon: "bi:phone-vibrate-fill", path: "/advertise" },
  { name: "Marketplace", icon: "solar:cart-4-bold", path: "/market-place" },
  {
    name: "Buy more followers & more",
    icon: "fluent:people-32-filled",
    path: "/buy-followers2",
  },
  { name: "Referral", icon: "ph:paper-plane-fill", path: "/referral" },
  {
    name: "My Dashboard",
    icon: "fluent:content-view-gallery-28-filled",
    path: "/dashboard",
  },
  { name: "My profile", icon: "bi:person-fill", path: "/my-profile" },
  { name: "FAQS", icon: "bxs:chat", path: "/frequency-asked-questions" },
  { name: "About us", icon: "fluent:info-12-filled", path: "/about2" },
  {
    name: "Chat with support",
    icon: "mdi:video-chat",
    path: "/chat-with-support",
  },
];

const SidebarContent = ({ onClose, ...rest }) => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const handleLogout = () => {
    dispatch(logout());
    navigate("/log-in");
  };
  return (
    <Box
      transition="3s ease"
      bg="#121212"
      maxW={{ base: "full", md: "25%" }}
      w={{ base: "full", md: "inherit" }}
      pos="fixed"
      top="0"
      h="full"
      pr={3}
      {...rest}
    >
      <Flex h="20" alignItems="center" mx="8" justifyContent="space-between">
        <Image src={Logo} />
        <CloseButton
          display={{ base: "flex", md: "none" }}
          onClick={onClose}
          color="white"
        />
      </Flex>
      <Box mt="10px" pb={20} maxH="100vh" overflowY="auto">
        {LinkItems.map((link) => (
          <NavItem
            key={link.name}
            icon={link.icon}
            path={link.path}
            onClose={onClose}
            pr="5"
          >
            {link.name}
          </NavItem>
        ))}
        <Box
        fontFamily="clash grotesk"
        p="10px 15px"
        color="white"
        onClick={handleLogout}
      >
        Log out
      </Box>
      </Box>
      
    </Box>
  );
};

const NavItem = ({ icon, children, path, onClose, ...rest }) => {
  const handleClick = () => {
    onClose(); // Close the mobile menu
  };
  const location = useLocation();
  const match = useMatch(path);

  // Determine if the NavLink should be active
  const isActive = () => {
    if (!match) return false; // Not active if not matched

    // Check if it's an exact match (top-level route) or a partial match (nested route)
    return (
      location.pathname === path || location.pathname.startsWith(path + "/")
    );
  };



  return (
    <Box>
      <NavLink
        to={path || "/homepage"}
        style={{ textDecoration: "none" }}
        onClick={handleClick}
        className={isActive() ? "active-nav-link" : "nav-link"}
      >
        <Flex
          align="center"
          p="0"
          mr="10"
          my="1"
          bg={isActive() ? "#762181" : "inherit"}
          color={isActive() ? "white" : "inherit"}
          fontFamily="clash grotesk"
          borderRadius="lg"
          fontSize="15px"
          borderBottomLeftRadius="none"
          borderTopLeftRadius="none"
          role="group"
          cursor="pointer"
          _hover={{
            bg: "#762181",
            color: "white",
          }}
          {...rest}
          pr={10}
        >
          {icon && (
            <iconify-icon
              icon={icon}
              style={{
                color: isActive() ? "white" : "inherit",
                margin: "10px",
              }}
              width="20"
              margin-right="10px"
            ></iconify-icon>
          )}
          {children}
        </Flex>
      </NavLink>
      {match?.route?.children && <Outlet />}
    </Box>
  );
};

const MobileNav = ({ onOpen, ...rest }) => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const handleLogout = () => {
    dispatch(logout());
    navigate("/log-in");
  };

  return (
    <Container
      maxW={{ xl: "100%", "2xl": "75%" }}
      bg="#121212"
      py="5"
      color="white"
      fontFamily="Clash Grotesk"
      className="mobile-header"
      justifyContent="space-between"
      display="flex"
      pos="fixed"
      mb="10"
    >
      <Flex alignItems="center" mx="8" justifyContent="space-between">
        <Image src={Logo} />
      </Flex>

      <Box
        display={{ base: "none", md: "flex" }}
        alignItems="center"
        border="1px solid #808080"
        borderRadius="15px"
        transition="border-color 0.3s ease"
        ml="4%"
      >
        <IconButton
          size="lg"
          variant="ghost"
          _hover={{ bg: "black", opacity: "0.9" }}
          aria-label="search"
          icon={<FiSearch color="white" />}
        />
        <Input
          type="text"
          placeholder="Search"
          bg="transparent"
          border="none"
          fontFamily="clash grotesk"
          outline="none"
          color="white"
          ml="-0"
          _focus={{
            borderColor: "transparent",
            boxShadow: "0 0 5px rgba(0, 0, 0, 0.2)",
          }}
        />
      </Box>

      <HStack spacing={{ base: "0", md: "6" }}>
        <IconButton
          size="lg"
          variant="ghost"
          mx="4"
          _hover={{ bg: "black", opacity: "0.9" }}
          aria-label="open menu"
          icon={<FiBell color="white" bg="#121212" />}
        />

        <Flex alignItems={"center"}>
          <Menu>
            <MenuButton
              py={2}
              transition="all 0.3s"
              _focus={{ boxShadow: "none" }}
              mr="6"
            >
              <HStack>
                {/* <Avatar size={"sm"} src={user.profile_picture} /> */}
                <VStack
                  display={{ base: "none", md: "flex" }}
                  alignItems="flex-start"
                  spacing="1px"
                  ml="2"
                >
                  <Text fontSize="sm" fontFamily="clash grotesk" color="white">
                    {/* {user.username} */}
                  </Text>
                </VStack>
                <Box display={{ base: "none", md: "flex" }}>
                  <FiChevronDown color="white" />
                </Box>
              </HStack>
            </MenuButton>
            <MenuList
              bg="black"
              p="0"
              fontFamily="clash grotesk"
              borderColor={useColorModeValue("gray.200", "gray.700")}
            >
              <MenuItem
                _hover={{
                  bg: "white",
                  color: "black",
                }}
                bg="black"
                p="10px 15px"
                borderTopRadius="5px"
                color="white"
              >
                Change Profile pics
              </MenuItem>
              <MenuItem
                _hover={{
                  bg: "white",
                  color: "black",
                }}
                bg="black"
                p="10px 15px"
                color="white"
              >
                Change password
              </MenuItem>
              <MenuItem
                _hover={{
                  bg: "white",
                  color: "black",
                }}
                bg="black"
                p="10px 15px"
                color="white"
                borderBottomRadius="5px"
                onClick={handleLogout}
              >
                Log out
              </MenuItem>
            </MenuList>
          </Menu>
        </Flex>

        <IconButton
          display={{ base: "flex", md: "none" }}
          onClick={onOpen}
          _hover={{ bg: "black", opacity: "0.9" }}
          variant="outline"
          aria-label="open menu"
          icon={<FiMenu color="white" />}
        />
      </HStack>
    </Container>
  );
};

const SidebarWithHeader = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const handleLogout = () => {
    dispatch(logout());
    navigate("/log-in");
  };
  const { isOpen, onOpen, onClose } = useDisclosure();

  return (
    <Box>
      <SidebarContent
        onClose={() => onClose}
        display={{ base: "none", md: "block" }}
      />
      <Drawer
        isOpen={isOpen}
        placement="left"
        onClose={onClose}
        returnFocusOnClose={false}
        onOverlayClick={onClose}
        size="full"
      >
        <DrawerContent>
          <SidebarContent onClose={onClose} />
        </DrawerContent>
      </Drawer>
      <MobileNav onOpen={onOpen} />
      <Box ml={{ base: 0, md: "25%" }} px="0">
        {/* Content */}
      </Box>
    </Box>
  );
};

export default SidebarWithHeader;
